s1 = input()
s2 = input()
lev_dist = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
for i in range(len(s2) + 1):
    lev_dist[i][0] = i
for j in range(len(s1) + 1):
    lev_dist[0][j] = j
for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        lev_dist[i][j] = min(lev_dist[i][j - 1] + 1,
                             lev_dist[i - 1][j] + 1,
                             lev_dist[i-1][j-1] + (0 if s2[i-1] == s1[j - 1] else 1))

print(lev_dist[-1][-1])
