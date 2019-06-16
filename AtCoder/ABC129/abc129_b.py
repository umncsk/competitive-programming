N = int(input()) # 個数
W = [int(x) for x in input().split()] # W(1) ~ W(N)

lst = []
for T in range(1, N):
    S1 = W[:T]
    S2 = W[T:]
    lst.append(abs(sum(S1) - sum(S2)))

print(min(lst))
