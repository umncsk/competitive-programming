N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

num = 0
for i in range(N+1):
    if num in a:
