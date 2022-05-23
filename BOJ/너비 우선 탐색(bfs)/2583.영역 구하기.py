from collections import deque
import sys
input = sys.stdin.readline
m, n, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            graph[x][y] = 1


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    area = 0
    while q:
        curr = q.popleft()
        x, y = curr[0], curr[1]
        area += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
    return area


visited = [[False]*m for _ in range(n)]
cnt = 0
area = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0 and not visited[x][y]:
            area.append(bfs(x, y))
            cnt += 1
area.sort()
print(cnt)
print(*area)
