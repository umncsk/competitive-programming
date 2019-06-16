n,m = map(int, input().split())
cards = []
for _ in range(m):
    l,r = map(int, input().split())
    cards.append([l,r])

counter = 0
all = []
for i in cards:
    for j in range(i[0], i[-1]):
        if j not in i:
            i.insert(j-1, j)
    all.extend(i)
    counter += 1

ans = 0
for q in all:
    if all.count(q) == m:
        ans += 1

print(round(ans/2))

