n = int(input())
a = [int(input()) for x in range(n)]

for i in range(n):
    if i == 0:
        s = 0
    else:
        s = i
    e = i + 1
    l = a[:s] + a[e:]
    print(sorted(l)[-1])
