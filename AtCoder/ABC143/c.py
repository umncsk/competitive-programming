n = int(input())
s = input()
dict = {}
for i,j in zip(range(0, n), s):
    dict[i] = j

for i in range(0, n - 1):
    if dict[i] == dict[i+1]:
        del dict[i]
        n -= 1
    else:
        continue
print(len(dict))
