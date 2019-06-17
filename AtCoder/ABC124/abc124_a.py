a,b = map(int, input().split())

coins = max(a,b)
if coins == a:
    a -= 1
elif coins == b:
    b -= 1
print(coins + max(a,b))
