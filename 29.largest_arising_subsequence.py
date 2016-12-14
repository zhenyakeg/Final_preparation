def LAS(A):
    n = len(A)
    l = [0] * n
    for i in range(n):
        for j in range(i):
            if l[j] > l[i] and A[j] < A[i]:
                l[i] = l[j]
        l[i] += 1
    return max(l)
print(LAS([1, 3, 4, 5, 7, 1, 9]))