n = int(input())
l = [x for x in map(int, input().split())]

cnt = 0
for i in range(0, n):
    a = l[i]

    if i == len(l) - 1:
        b = l[0]

        for j in range(0, n):
            c = l[j]
            if j == 0 or j == i:
                continue
            else:
                if a < b + c and b < c + a and c < a + b:
                    cnt += 1
                else:
                    continue

    else:
        b = l[i + 1]

        for j in range(0, n):
            c = l[j]
            if i + 1 == j or i == j:
                continue
            else:
                if a < b + c and b < c + a and c < a + b:
                    cnt += 1
                else:
                    continue

print(cnt)
