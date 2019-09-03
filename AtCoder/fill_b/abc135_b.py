n = int(input())
p = list(map(int, input().split()))

diff = 0
for i,j in zip(range(1, n+1), p):
    if i != j:
        diff += 1
if diff <= 2:
    print("YES")
else:
    print("NO")
