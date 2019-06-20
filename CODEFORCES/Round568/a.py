a,b,c,d = map(int, input().split())

ans = 0
l = sorted([a,b,c])

if d > abs(l[0] - l[1]):
    ans += d - abs(l[0] - l[1])
if d > abs(l[1] - l[2]):
    ans += d - abs(l[1] - l[2])

print(ans)