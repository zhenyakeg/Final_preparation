s = input()


def z_function(s):
    l, r = 0, 0
    z = [0] * len(s)
    for i in range(1, len(s)):
        x = (min(z[i - l], r - i + 1) if i <= r else 0)
        # x = z[i - l] if i <= r else 0
        while i + x < len(s) and s[x] == s[i + x]:
            x += 1
        z[i] = x
        if i + x - 1 > r:
            l, r = i, i + x - 1
    return z

print(' '.join(map(str, z_function(s))))

'abaabahhhhhabaabl - пример с выходом за рамку'
'0 0 1 3 0 1 0 0 0 0 0 5 0 1 3 0 1'
'0 0 1 3 0 1 0 0 0 0 0 5 0 1 2 0 0'
