n = int(input())
a = [int(x) for x in input().split()]

ans = 0
while True:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
        else:
            print(ans)
            exit()
    ans += 1

print(ans)