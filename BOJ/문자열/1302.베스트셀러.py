import sys, collections
input = sys.stdin.readline
n = int(input())
books = []
for _ in range(n):
    books.append(input().rstrip())

best = collections.Counter(books)
best = sorted(best.items(), key=lambda x: (-x[1], x[0]))
print(best[0][0])