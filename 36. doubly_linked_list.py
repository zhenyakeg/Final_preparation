class doubly_linked__list():
    def __init__(self):
        self.begin = None
        self.end = None
    def push_front(self, data):
        if self.begin == None:
            self.begin = self.end = [None, data, None]
        else:
            tmp = [None, data, self.begin]
            self.begin[0] = tmp
            self.begin = tmp
    def pop_end(self):
        if self.end == None:
            raise IndexError
        result = self.end[1]
        if self.end[0] == None:
            self.end = self.begin = None
        else:
            #print(self.end[0])
            self.end = self.end[0]
            self.end[2] = None
        return result

'''Последовательность для пуша: Если начальный список пуст, создаем первый узел, начало и конец одинаковые. если
список уже не пустой -> создаем временную заготовку с новым элементом, меняем ссыслку в прежнем начале на новую
заготовку и делаем новым началом то, что до этого было заготовкой.'''

'''Схема  пуша: Пуст - ошибка, один элемент - возвращаем его, обнуляем начало и конец, если элементов несколько
 то из конца берем элемент, а новый конец делаем нулевой ссылкой из предыдущего конца, и правую часть нового конца делаем пустым'''

'''36. Двусвязный список на Python. Очередь.'''