n = int(input())
l = [x for x in map(int, input().split())]
l = sorted(l)

cnt = 0
for i in range(n - 2):
    a = l[i]
    k = i + 2
    for j in range(i + 1, n - 1):
        b = l[j]
        while(l[k] < a + b):
            k += 1
            if k == n:
                break
            else:
                pass

        k -= 1
        cnt += k - j
print(cnt)
