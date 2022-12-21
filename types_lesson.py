import logging

logging.StreamHandler()


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

target = '{{[()]]'

def check_br(inp: str):
    match = {'(':')','[':']','{':'}'}

    op = Stack()
    # clo = Stack()

    for i in inp:
        logging.warning(op.show())

        if i in match.keys():
            op.put(i)

        elif i in match.values():
            
            if len(op) and (match[op.pop_item()] == i):
                print(op.show())
            else:
                logging.warning(inp.index(i) + 1)  
                return inp.index(i)+1
        else: continue
    return 'success'


check_br(target)