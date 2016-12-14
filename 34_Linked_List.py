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

    '''При добавлении просто создается новый массив с элементом и связью вперед. При откусывании
    сохраняется предыдущий конец, а новый создается из ссылки'''
a = LinkedList()
a.push_front(50)
a.pop_front()
print(a.empty())

'''34. Односвязный список на Python. Реализация при помощи класса LinkedList. Ассимптотика операций.'''