n = int(input())
book = []
for _ in range(n):
    s,p = input().split()
    book.append((s.strip(), int(p)))

rank = sorted(book, key=lambda x: (x[0], -x[1]))
for i in rank:
    print(int(book.index(i)) + 1)
