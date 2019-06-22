n,l = map(int, input().split())
aji_apple = [l + x - 1 for x in range(1,n+1)]

aji_pie = []
for i in range(0,n):
    v = abs(sum(aji_apple) - (sum(aji_apple) - aji_apple[i]))
    aji_pie.append(v)

min_index = aji_pie.index(min(aji_pie))

print(sum(aji_apple) - aji_apple[min_index])

