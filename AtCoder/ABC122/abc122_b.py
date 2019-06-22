# AtCorder

s = input()

a = "ACGT"
v = 0
ans = 0

for i in s:
    if i in a:
        v += 1
        ans = max(ans, v)
    else:
        v = 0

print(ans)