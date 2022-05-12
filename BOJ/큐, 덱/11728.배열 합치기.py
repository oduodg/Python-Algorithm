import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
a = deque(list(map(int, input().split())))
b = deque(list(map(int, input().split())))
ans = []
while a and b:
    if a[0] <= b[0]:
        ans.append(a.popleft())
    else:
        ans.append(b.popleft())

if a:
    ans += list(a)
if b:
    ans += list(b)
print(*ans)
