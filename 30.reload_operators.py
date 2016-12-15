class Some_class:
    def __init__(self, A):
        self.body = A
        """Класс спец массивов, хотим сравнивать такие массивы с числами, и операции делать с числами"""

    def __add__(self, data):
        self.body.append(data)
        return self
        """Прибавлять к элементам класса можно числа, они просто добавляются в массив"""

    def __sub__(self, data):
        if data in self.body:
            self.body.pop(self.body.index(data))
        return self
        """При вычитании просто возвращается массив без элемента который вичитался, если он был в массиве,
        если не было ничего не изменится"""

    def __mul__(self, other):
        for i in self.body:
            i *= other
        return self
        '''При умножении возвращается список с умноженными элементами'''

    def __truediv__(self, other):
        for i in self.body:
            i /= other
        return self
        '''При делении все элементы делятся  на делитель'''

    def __lt__(self, other):
        for i in self.body:
            if i >= other:
                return False
        return True
        '''Массив меньше, если все элементы меньше'''

    def __eq__(self, other):
        for i in self.body:
            if i != other:
                return False
        return True
        '''Аналогично равен, если все равны'''

    def __gt__(self, other):
        for i in self.body:
            if i <= other:
                return False
        return True
        '''Массив больше, если все элементы больше'''

    def __str__(self):
        return 'SPECIAL LIST'
    '''То что вернет функция str'''

    def __repr__(self):
        return 'PRINTED SPECIAL LIST'
    '''То, что выведет print'''

B = Some_class([1, 2])
B = B + 3
B = B + 4
B = B - 1
B = B - 2
B.pipirka = 5
s = B.pipirka
C = Some_class([])
print(str(B))

'''30. Перегрузка операторов для классов в Python.'''
