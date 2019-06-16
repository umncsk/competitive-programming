n = int(input())
c = []
for _ in range(n):
    x,y = map(int, input().split())
    c.append((x,y))

# define p,q
for c_ in c:
    if c_[0] != c[0][0]:
        p = c_[0] - c[0][0]
        q = c_[1] - c[0][1]
        break

cost = 1
counter = 0
for i in reversed(c):
    if counter == 0:
        even = i
        counter += 1
        continue
    else:
        even_ = (even[0]-p, even[1]-q)
        if even_ == i:
            even = i
            continue
        else:
            cost += 1

print(cost)
