n,k = map(int, input().split())
a = [int(x) for x in input().split()]

ans = 0
for i in range(n):
    for j in range(i+1,n):
        if sum(a[j-i:]) >= k:
            ans += 1
        if sum(a[:j-i]) >= k:
            ans += 1

print(ans)