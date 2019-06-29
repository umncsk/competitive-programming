n = int(input())
d = list(map(int, input().split()))

d = sorted(d)

print(d[round(len(d) / 2)] - d[round(len(d) / 2) - 1])