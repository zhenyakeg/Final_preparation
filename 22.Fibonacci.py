def Fibonacci_recursion (n):
    if n == 1 or n == 2:
        return 1
    return Fibonacci_recursion(n-2) + Fibonacci_recursion(n-1)
def Fibonacci_cycle (n):
    A = [0] * (n+1)
    A[1], A[2] = 1, 1
    for i in range (3,n+1):
        A[i] = A[i-2] + A[i-1]
    return A[n]
'''Рекурсивный алгоритм асимптотика O(Fibonacci(n))
Динамический алгоритм асимптотика O(n)'''

'''Вычисление чисел Фибоначчи. Реализация на Python через цикл и через рекурсию.'''
print(Fibonacci_cycle(7))
