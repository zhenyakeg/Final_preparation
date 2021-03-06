A = [i for i in range(2000000000)]
def monkey_sort(A):
    import random as rnd
    while not A == sorted(A):
        rnd.shuffle(A)
    return A
'''10. Сортировка обезъяны.
    Ассимптотика алгоритма O(N*N!) - среднее время'''

def insertion_sort(A):
    for  i in range(1, len(A)):
        tmp = A[i]
        k = i-1
        while k >= 0 and A[k] > tmp:
            A[k+1] = A[k]
            k -= 1
        A[k+1] = tmp
    return A
'''11. Сортировка вставками. Вставка элемента в отсортированный подмассивв
    Асимптотика O(N^2). Устойчивая. Проходим по списку,
     берем элемент, временно сохраняем, если слева стоят элементы большие,
     сдвигаем вправо, в итоге массив окажется отсортированным по возрастанию'''

def choice_sort(A):
    for i in range (len(A)-1):
        for k in range (i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]
    return A
'''12. Сортировка выбором.
    Асимптотика O(N^). Устойчивая. Поиск минимума в подмассиве, начиная с i. Инвариант: все, что до i отсортировано.
    Берем элемент и смотрим есть ли справа меньшие, если есть, меняем и так  пробегаем по всемю'''

def bubble_sort(A):
    for i in range(1, len(A)):
        for k in range(len(A) - i):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A
'''13. Сортировка пузырька. Асимптотика O(N^2). Учтойчивая.
    Проходим
     +..весь массив. За первый проход самый большой окажется на самом высоком месте
    потом сортируем также массив кроме пооследнего элемента(экономия операций)'''

def fool_sort(A):
    i = 0
    while i < len(A) - 1:
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            i = 0
        else:
            i+=1
    return A
'''14. Сортировка дурака. Асимптотика O(N^3). Устойчивая.
    Сравниваем i и i+1 если они не правильно расположены, меняем местами и начинаем с начала.
    Так первый элемент отсортируется за N^2 операций, дальше еще N-1 элементов которые будут сортироваться за (N-i)^2.
    В итоге N^3'''

def count_sort(A):
    M  = max(A) #Хорошо, когда мы заранее знаем, ограничение чисел в массиве
    Q = [0]*(M+1)
    for x in A:
        Q[x] += 1
    pos = 0
    for i in range(M+1):
        for k in range(Q[i]):
            A[pos] = i
            pos += 1
    return A
'''15. Сортировка подсчетом. Асимптотика O(M+N). НЕУСТОЙЧИВА. Массив генерируется заново.
    Удобно использовать если M мало. Мы проходим и считаем сколько раз каких чисел встречалось.
    Потом просто проходим по всем возможным числам и смотрим в массив подсчета и выписываем в конечный массив число
    столько раз, сколько оно встречалось.'''

def radix_sort(A):
    max_len = len(str(max(A)))
    for i in range(max_len):
        B = [[] for i in range(10)]
        for x in A:
            digit = (x // 10 ** i) % 10
            B[digit].append(x)
        A[:] = []
        for k in range(10):
            A.extend(B[k])
    return A
'''16. Поразрядная сортировка. O(max_len*N). Устойчива. Для небольших max_len обгоняет даже быстрые сортировки.
    Создаем поразрядный массив из массивов и записываем туда поразрядно числа из А, потом записываем их в новый А и так по возрастанию разряда.
    В итоге  отсортируем массив.'''

def hoar_sort(A):
    if len(A) <= 1:
        return A
    import random as rnd
    barrier = rnd.choice(A)
    L, M, R = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        elif x > barrier:
            R.append(x)
    return hoar_sort(L) + M + hoar_sort(R)
'''17. Быстрая сортировка Хоара. РЕКУРРЕНТНАЯ. Ассимптотика максимальная квадратичная,
    но средняя N*Log(N) и требует всего O(1) доп. памяти. Интуитивно понятная.
    Если массив из одного элемента - отсортирован. Назначаем в массиве любой элемент барьерным
    дальше преребираем элементы массива, если они меньше барьерного, записываем в список слева, если больше
    вправо, если равны, записываем в список равных, дальше сортируем левый и правый, после чего возвращаем А'''

def merge_sort(A):
    if len(A) <= 1:
        return A
    L = merge_sort(A[:len(A)//2])
    R = merge_sort(A[len(A)//2:])
    return merge(L, R)
def merge(L, R):
    A = [None]*(len(L)+len(R))
    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[i]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    A[k:] = L[i:] + R[j:]
    return A

'''18. Сортировка слиянием. Устойчива. O(N*log(N)).
    Делим массив на две части, каждую из них сортируем и сливаем вместе
    при этом слияние происходит особым образом: выбирается элемент из  левого массива
    и сравнивается с элементом из правого
    меньший записывается в ячейку А, потом смотрим следующий из меньшего, пока не дойдем до конца одного из списков
    ну и дополняем А остатком. По сути делим массив на элементы одиночные, их сравниваем, а потом сливаем, но при этом длина
    все время делится на два поэтому и ассимптотика такая.'''

print(count_sort(A))

