def circle_change_simple(A):
    tmp = A[-1]
    for i in range(0, len(A)-1):
        A[len(A)-i-1] = A[len(A)-i-2]
    A[0] = tmp
    return A
    '''Цикличиский сдвиг массива вправо'''


'''Алгоритм циклического сдвига в массиве. Реализация на Python.'''
