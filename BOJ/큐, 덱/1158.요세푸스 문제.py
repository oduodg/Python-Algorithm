from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

l = [i for i in range(1, n+1)]
d = deque(l)
answer = []

cnt = 1

while d:
    if cnt == k:
        answer.append(d.popleft())
        cnt = 1
    else:
        d.append(d.popleft())
        cnt += 1

print('<', end='')
print(*answer, sep=', ', end='>')
