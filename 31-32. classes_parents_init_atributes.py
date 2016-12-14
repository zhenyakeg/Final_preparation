import random
class Animal:
    def __init__(self, sex='male', name= 'sf', size=1):
        self.size = size
        self.sex = sex
        self.name = name
        '''классовые атрибуты открытые'''
        self.__DNA = 'a'
        '''закрытый атрибут'''
    def hungry(self):
        print('HUNGRY!!!')
    def repoduction(self, other):
        Child = Animal(sex=random.choice(['m','f']), size=self.size+other.size, name= self.name + other.name)
        Child.__DNA = self.__DNA + other.__DNA
        return Child

class Fish(Animal):
    def __init__(self, sex='male', name= 'sf', size=1, len_of_swimmers=2):
        super(Fish, self).__init__(sex, name, size)
        self.len_of_swims = len_of_swimmers
        '''такой конструктор создает объект класса Animal, то есть запускае его конструктор, таким образом можно
        не прописывать заново конструктор животного, а просто скормить ему нужные параметры, можно super писать
        без параметров, делает то же самое'''
    def change_sex(self):
        self.sex = 'female'
        return self
f1 = Fish('maaaale', 'Dory', 55, 33)
f2 = Fish('female', 'peter', 48, 99)
print(f1.sex)
f2.change_sex()
print(f2.sex)

'''31. Конструктор класса в Python. Классовые и экземплярные атрибуты.
   32. Наследование классов в Python. Вызов конструктора надкласса.'''