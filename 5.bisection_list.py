def bisection_search(A, x):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right)//2
        if A[middle] > x:
            right = middle
        else:
            left = middle

    if A[right-1] == x:
        print('Found. Index:', right - 1)
        return
    else:
        print ('Not found')
    '''На вход подается отсортирванный массив при этом A[right] всегда > х,
    а A[left] <= x, таким образом если элемент в массиве есть, такой поиск выдаст
    последнее вхождение элемента, если инвариант цикла взять другим, то вернет первое вхождение,
    ассимптотика поиска log2(len(A))
    быстрый аналог index для отсортирванных массивов'''
A = [5 for i in range(99990)]
bisection_search(A, 5)