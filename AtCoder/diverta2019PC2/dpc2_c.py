n = int(input())
a = [int(x) for x in input().split()]

a = sorted(a)

ans = max(a) - min(a)

a = a[1:-1]

for i in a:
    if i < 0:
        ans += i
    if i > 0:
        ans += i

print(ans)