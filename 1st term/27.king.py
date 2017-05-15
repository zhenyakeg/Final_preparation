def king_count_trajectories(M,N):
    Field = [[0 for i in range(M+1)] for j in range (N+1)]
    Field[0][0] = 1
    for i in range(1, N+1):
        for j in range(1,M+1):
            Field[i][j] += Field[i][j-1] + Field[i-1][j] + Field[i-1][j-1]
    return Field[-1][-1]
print(king_count_trajectories(8, 8))


'''27. Двумерное динамическое программирование. Задача о количестве траекторий шахматного короля. Реализация на Python.'''