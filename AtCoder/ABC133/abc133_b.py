import math #math.sqrt(x)

n,d = map(int, input().split())
x = []
for _ in range(n):
    x.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for q in range(n):
        sumv = 0
        if i == q:
            continue
        for j in range(d):
            sumv += (x[i][j] - x[q][j]) ** 2

        if math.sqrt(sumv).is_integer() == True:
            ans += 1

print(round(ans/2))
