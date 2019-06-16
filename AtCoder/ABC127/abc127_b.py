r,d,x = map(int, input().split())

for i in range(0, 10):
    print(r * x - d)
    x = r * x - d
