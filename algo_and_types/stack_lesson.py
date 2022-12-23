match = {'(': ')', '[': ']', '{': '}'}

class Stack(list):
    def __init__(self):
        super().__init__()

    def put(self, item, index_item):
        self.append([item, index_item])

    def pop_item(self):
        if self:
            return self.pop()
        else:
            return ''

    def show(self):
        return self


target = input()


def check_br(inp: str):

    op = Stack()
    count = 0
    for i in inp:
        count += 1

        if i in match.keys():
            op.put(i, count)

        elif i in match.values():
            if len(op) and (match[op.pop_item()[0]] == i):
                continue
            else:
                return count
        else:
            pass

    if op.show() != []:
        return op.pop_item()[1]
    else:
        return 'Success'


print(check_br(target))
