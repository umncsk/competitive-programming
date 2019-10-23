n = int(input())
a = [x for x in map(int, input().split())]

dic = {}
for i in range(n):
    dic[i + 1] = a[i]

dic_sorted = sorted(dic.items(), key=lambda x:x[1])

ans = ""
for i in dic_sorted:
    ans = ans + ' ' + str(i[0])

print(ans)
