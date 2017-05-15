vertex1, vertex2 = map(int, input().split())
m = int(input())
tree = [[] for j in range(m + 1)]
for j in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
def is_child(tree, start, finish):
    q = [start]
    while q:
        current = q.pop(0)
        for child in tree[current]:
            if finish == child:
                return True
            q.append(child)
    return False
if is_child(tree, vertex1, vertex2):
    print('YES')
else:
    print('NO')