a,b = map(int, input().split())

ans = 0
cnt = 1
while cnt < b:
    cnt += a - 1
    ans += 1
print(ans)
