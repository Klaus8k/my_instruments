
match = {'(':')','[':']','{':'}'}

class Stack(list):
    def __init__(self) :
        super().__init__()
    
    def put(self, item):
        self.append(item)

    def pop_item(self):
        if self:
            return self.pop()
        else: return ''

    def show(self):
        return self

target = input()

def check_br(inp: str):

    op = Stack()
    # clo = Stack()
    err_index = 1
    count = 0
    for i in inp:
        count += 1
        # logging.warning(op.show())

        if i in match.keys():
            op.put(i)

        elif i in match.values():
            # logging.warning(i)
            if len(op) and (match[op.pop_item()] == i):
                err_index += 1
            else:
                # logging.warning(count)  
                return count
        else: pass

    if op.show() != []:
        return err_index
    else: 
        return 'Success'


print(check_br(target))