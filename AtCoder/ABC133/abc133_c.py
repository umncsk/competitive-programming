l,r = map(int, input().split())

minv = 1145141919810931
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        minv = min(minv, (i * j) % 2019)

print(minv)