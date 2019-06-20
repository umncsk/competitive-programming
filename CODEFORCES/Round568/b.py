n = int(input())
l = [input() for x in range(2 * n)]

for i in range(0, n * 2, 2):
    lv1 = set(list(l[i]))
    lv2 = set(list(l[i + 1]))
    if lv1 == lv2:
        print("YES")
    else:
        print("NO")