a,b = map(int, input().split())

if a >= 13:
    print(b)
if a >= 6 and a <= 12:
    print(round(b/2))
if a <= 5:
    print(0)