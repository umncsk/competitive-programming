n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, len(p) - 1):
    setv = p[(i - 1) : (i + 2)]
    setv_mid = setv[1]
    if sorted(setv)[1] == setv_mid:
        ans += 1

print(ans)