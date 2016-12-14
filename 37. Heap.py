class Heap:
    def __init__(self):
        self.body = []
    def heap_push(self, x):
        self.body.append(x)
        i = len(self.body) - 1
        while i != 0:
            ip = (i-1) // 2
            if self.body[i] <= self.body[ip]:
                break
            else:
                self.body[i], self.body[ip] = self.body[ip], self.body[i]
                i = ip

    def heap_pop(self):
        if len(self.body) == 1:
            return self.body.pop()
        retval = self.body[0]
        self.body[0] = self.body.pop()
        i = 0
        while 2 * i + 2 < len(self.body) and self.body[i] < max(self.body[2 * i + 1], self.body[2 * i + 2]): #Есть оба родителя, присем один из них меньше ребенка
            if self.body[2 * i + 1] > self.body[2 * i + 2]:
                self.body[i], self.body[2 * i + 1] = self.body[2 * i + 1], self.body[i]
                i = 2 * i + 1
            else:
                self.body[i], self.body[2 * i + 2] = self.body[2 * i + 2], self.body[i]
                i = 2 * i + 2
        if 2 * i + 1 == len(self.body) - 1 and self.body[i] < self.body[2 * i+1]: #Нет правого, но левый больше  ребенка
            self.body[i], self.body[2 * i + 1] = self.body[2 * i + 1], self.body[i]
        return retval

a = Heap()
A = [9, 9]
for x in A:
    a.heap_push(x)
print(a.body)
for i in range (len(A)):
    c = a.heap_pop()
    print(c)

print(a.body)
'''Описание пуша. добавляем в конец списка элемент. вычисляем его индекс, мы знаем индекс родителя. пошли вверх.
Как только родитель становится больше либо равен текущего выходим из цикла иначе меняем ребенка и родителя  местами.

Описание попа: если в куче один элемент возвращаем его и удаляем. Если правый ребенок есть и родитель меньше этого ребенка,
идем вниз, меняясь с ним, или с левым, выбираем по максимуму из них. Если правого нет, проверяем, что левый ребенок больше и меняемся'''
'''(i-1)//2 - Родитель
         i*2 + 1 левый ребенок
         i*2 + 2 правый ребенок'''