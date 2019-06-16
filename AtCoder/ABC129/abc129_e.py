L = input()

intL = int(L)
L10 = int(L, 2)
sum_ = 0
for a in range(L10+1):
    for b in range(L10+1):
        if ((a + b) <= L10) and ((a + b) == (a ^ b)):
            sum_+=1

print(sum_ % (10**9 + 7))
