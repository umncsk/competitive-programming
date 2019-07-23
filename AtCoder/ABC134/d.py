from math import sqrt
n = int(input())
a = list(map(int, input().split()))

ans = {}
for i in range(1, n+1):
    xs = []
    for j in range(i-1, n, i):
        xs.append(a[j])
    ans[i] = sum(xs) % 2

print(max(ans.items(), key = lambda x:x[1])[0])
print(max(ans.values()))
