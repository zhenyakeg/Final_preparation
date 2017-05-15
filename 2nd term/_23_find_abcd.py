s = input()
state = 0
i = 0
for letter in s:
    if letter == 'a':
        state = 1
    elif letter == 'b' and state == 1:
        state = 2
    elif letter == 'c' and state == 2:
        state = 3
    elif letter == 'd' and state == 3:
        state = 4
        print("found:", i - 3)
    else:
        state = 0
    i += 1
