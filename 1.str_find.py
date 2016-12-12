def str_find(s,sub):
    for i in range(len(s)-len(sub)+1):
        for k in range(len(sub)):
            if s[i+k] != sub[k]:
                break
        else:
            return i
    return -1
'''Наивный поиск подстроки в строке. Реализация на Python без использования стандартных методов str.'''
