def count_trajectories(n):
    k =[1, 1]
    for i in range(2, n+1):
        k.append(k[i-2] + k[i-1])
    return k[n]
    '''Кузнечик может прыгать либо на следующую клетку, либо через
    одну, тогда число траекторий в точку i складываетсся из
    числа траекторий в предыдущую точку и через одну наза'''

def trajectory_min_cost(Price, n):
    c = [0, Price[0]]
    for i in range(2,n+1):
        c.append(Price[i-1] + min(c[i-2], c[i-1]))
    return c[n]

def trajectory (Cost, n):
    traj = [n]
    while traj[-1] != 0:
        current = traj[-1]
        if Cost[current - 1] < Cost[current-2]:
            traj.append(current-1)
        else:
            traj.append(current-2)
    return traj[::-1]
    '''Минимальная стоимость попадания на i место складывается из цены этого места и минимума между
    стоимостями предыдущего места и места через один назад, восстанавливать траекторию удобнее всего с конца, выбирая самые дешевые ступени'''

def trajectory_cost_list(Price, n):
    c = [0, Price[0]]
    for i in range(2, n + 1):
        c.append(Price[i - 1] + min(c[i - 2], c[i - 1]))
    return c
print(count_trajectories(2))
# print(trajectory(trajectory_cost_list([4, 3, 5, 6, 6, 4,3], 5), 5))

'''25. Задача о количестве траекторий Кузнечика на числовой прямой. Реализация на Python.

    26. Задача о траектории наименьшей стоимости для Кузнечика. Восстановление траектории наименьшей стоимости. Реализация на Python.'''