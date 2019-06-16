n = int(input())
r = []
for _ in range(n):
    r.append(int(input()))

maxv = -float("inf")
minv = r[0]
for i in range(1, n):
    maxv = max(maxv, r[i] - minv)
    minv = min(minv, r[i])

print(maxv)