from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bad = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    bad[x].append(y)
    bad[y].append(x)

cnt = 0

for i in range(1, n-1):
    for j in range(i+1, n):
        if j in bad[i]:
            continue
        for k in range(j+1, n+1):
            if k in bad[i]:
                continue
            elif k in bad[j]:
                continue
            else:
                cnt +=1
print(cnt)