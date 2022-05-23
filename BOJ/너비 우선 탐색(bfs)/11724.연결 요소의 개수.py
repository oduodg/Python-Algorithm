from collections import deque
from re import M
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)


def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        x = q.popleft()

        for next in graph[x]:
            if not visited[next]:
                q.append(next)
                visited[next] = True


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
