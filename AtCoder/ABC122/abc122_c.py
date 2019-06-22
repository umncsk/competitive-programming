n,q = map(int, input().split())
s = input()
l = [0] * q
r = [0] * q
for num in range(q):
    l[num],r[num] = map(int, input().split())

for i in range(0,q):
    start = l[i] - 1
    end = r[i]
    strv = s[ start:end ]

    ans = 0
    for j in range(0,len(strv) - 1):
        if strv[j] == "A" and strv[j + 1] == "C":
            ans += 1

    print(ans)