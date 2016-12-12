def bisection(f , a, b, eps):
    try:
        assert (f(a)*f(b) <= 0)
    except:
        print("Can't find roots")
        return
    while (b-a) > 2*eps:
        c = (a+b)/2
        for p in a,b,c:
            if f(p) == 0:
                print(p)
                return
        else:
            if f(c)*f(b) <= 0:
                a,b = c,b
            else:
                a, b = a, c
    print((a+b)/2)
    '''Функция должна быть непрерывна и принимать на концах значения разных знаков,
    по теореме Больцано-Коши есть точка где значение = 0 будем сокращать отрезок пополам
    при этом надо проверять что мы не попали в ноль при делении или на краях отрезка, если попали - выводим a, b, c.
    Сокращаем до тех пор пока  не достигнем нужной точности
    Асимптотика: log2((b-a)/eps)'''

'''4. Поиск корня уравнения методом бисекции. Требования алгоритма к функции. Реализация на Python и ассимптотика алгоритма.'''

f = lambda x: x
bisection(f, 0, 300, 0.0000001)