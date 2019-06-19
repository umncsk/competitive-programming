n = int(input())
r = [int(input()) for x in range(n)]

minv = r[0]
maxv = -float("inf")
for i in range(1, n):
    maxv = max(maxv, r[i] - minv)
    minv = min(minv, r[i])

print(maxv)