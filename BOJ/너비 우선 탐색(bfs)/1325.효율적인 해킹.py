from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

cnt = [0] + [1 for _ in range(n)]

def bfs(x):
    visited = [False for _ in range(n+1)]
    q = deque([x])
    visited[x] = True

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                cnt[x] += 1
                visited[next] = True

maxCnt = 1
ans = []
for i in range(1, n+1):
    bfs(i)
    if cnt[i] > maxCnt:
        maxCnt = cnt[i] # max 갱신
        ans.clear() # ans 초기화
        ans.append(i)
    elif cnt[i] == maxCnt:
        ans.append(i)

print(*ans)