def GCS(a,b):
    n = len(a)
    m = len(b)
    l = [[0]*(m+1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    return l[n][m]
    ''' Массив создан больше чтобы не делать проверку на первый элемент.
    Мы создаем двумерный массив m - столбцов, n- строк; i, j элемент - длина максимальной общей
    подпоследовательности между кусками последовательностей до i и j соответсственно, смотрим, если очередные
    элементы совпали, то наибольшая общая подпоследовательность равна наибольшей большей подпоследовательности
    из последовательностей на один меньшей длины плюс один, так как нашли еще один общий элемент, если элементы не совпали,
    максимальная подпоследовательность либо сосставлена из наибольшей подпоследовательности в которой один из индексов смещен назад
    то есть берется последовательность а до i элемента а b до j-1, так получаем все длины наибольших подпоследовательностей.
    Асимптотика O(M*N) по операциям и O(M*N) по памяти.'''

    '''28. Наибольшая общая подпоследовательность. Ассимптотика алгоритма. Реализация.'''

print(GCS('loshadky', 'osedlal'))