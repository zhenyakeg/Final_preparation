def evklid_recursion(a, b):
    if b == 0:
        return a
    return evklid_recursion(b, a%b)
'''Если два числа делятся на третье число, то разность этих чисел тоже делится на это число,
будем вычитаать из первого второе максимальное количество рааз и брать то, что осталось, в итоге одно из чисел
дойдет до нуля и мы получим в качестве второго НОД'''
def evklid_cycle_clever(a,b):
    while b > 0:
        a, b = b, a%b
    return a
def evklid_cycle_stupid (a,b):
    if a == b:
        return a
    while a!=b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
print(evklid_cycle_stupid(11,12))

'''20. Алгоритм Евклида. Реализация на Python через цикл и через рекурсию.'''