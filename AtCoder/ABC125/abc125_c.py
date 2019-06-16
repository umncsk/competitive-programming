n = int(input())
a = [int(x) for x in input().split()]

a = sorted(a)

a_odd = []
for l in a:
    if l%2 == 1:
        a_odd.append(l)

odd_max = max(a_odd)