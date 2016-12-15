def hanoi(n, i = 1 , k = 3):
    if n == 1:
        print(n, i, k)
    else:
        print(n, i, k)
        tmp = 6 - i -k
        hanoi(n-1,i, tmp)
        hanoi(n-1, tmp, k)
hanoi(68)
'''Асимптотика O(2^N - 1)'''

'''23. Ханойские башни. Алгоритм и его реализация на Python.'''