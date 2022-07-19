import sys
input = sys.stdin.readline

n = int(input())
stuff = []
ans = 0

for _ in range(n):
    stuff.append(int(input()))

stuff.sort(reverse=True)

for i in range(n):
    if i >= n//3 * 3:
        ans += stuff[i]
        continue

    if i % 3 == 2:
        continue
    else:
        ans += stuff[i]

print(ans)
