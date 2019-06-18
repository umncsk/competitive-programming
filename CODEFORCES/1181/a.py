a,b,c = map(int, input().split())

if a % c > b % c:
    a += (b % c)
    e = (b % c) - (a % c)
else:
    b += (a % c)
    e = (a % c) - (b % c)

if e < 0:
    e = 0

print((a // c) + (b // c), e)