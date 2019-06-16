n,x = map(int, input().split())
l = [int(x) for x in input().split()]

ans = 1
d = 0
for i in range(1, n+1):
    d += l[i-1]
    if d <= x:
        ans += 1
    else:
        break

print(ans)