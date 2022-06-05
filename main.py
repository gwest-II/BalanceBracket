

class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self, el):
        self.item.append(el)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]test

    def size(self):
        return len(self.item)


def balance_bracket(str):
    stack = Stack()
    pushBracket, popBracket = '<({[', '>)}]'
    for c in str:
        if c in pushBracket:
            stack.push(c)
        elif c in popBracket:
            if stack.isEmpty():
                return False
            else:
                stack_top = stack.pop()
                balancing_bracket = pushBracket[popBracket.index(c)]
                if stack_top != balancing_bracket:
                    return "Несбалансированно"
        else:
            return "Несбалансированно"
    else:
        return "Сбалансированно"



if '__main__' == __name__:

    print(balance_bracket('()'))
