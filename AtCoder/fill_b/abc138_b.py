n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    a[i] = 1/a[i]
print(1/sum(a))

