class LinkedList:
    def __init__(self):
        self.__begin = None
    def push_front(self, data):
        p = self.__begin
        self.__begin = [data, p]
        '''O(1)'''
    def pop_front(self):
        if self.__begin == None: #Not self.__begin
            raise IndexError
        else:
            data = self.__begin[0]
            self.__begin = self.__begin[1]
            return data
        '''O(1)'''
    def empty(self):
        return not self.__begin

def analise_brakets_sequence(s):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    pair = dict(zip(left,right))
    stack = LinkedList()
    for brace in s:
        if brace in left:
            stack.push_front(brace)
        else:
            if stack.empty():
                return False
            else:
                if pair[stack.pop_front()] != brace:
                    return False
    return stack.empty()
print(analise_brakets_sequence('()[]{}[[[{}]]]'))

'''Если скобка добавляется в стек, то она левая, если попалась правая в стеке должна лежать соответствующая,
если в конце сскобок в стеке не осталось, все хорошо.'''

'''35. Стек. Использование стека для проверки корректности скобочной последовательности.'''
