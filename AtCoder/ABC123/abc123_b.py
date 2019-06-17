menu = [int(input()) for x in range(5)]

t = 0
d = 0
for i in menu:
    if i % 10 == 0:
        t += i
    elif round(i, -1) > i:
        t += round(i, -1)
    else:
        t += round(i, -1) + 10
    d = max(d, 10 - round(i, -1))


print(t - d)