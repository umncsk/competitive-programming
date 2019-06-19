n = int(input())
a = [int(x) for x in input().split()]

for i in range(1, n):
    v = a[i]
    for j in range(i - 1, -1, -1):
        if a[j] > v:
            a[j + 1] = a[j]
        elif j == -1 or a[j] <= v:
            break

    a[j + 1] = v

    print(" ".join([str(x) for x in a]))
