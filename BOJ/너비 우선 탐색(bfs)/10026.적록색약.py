from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = []  # 적록색약 아닌 사람
for _ in range(n):
    graph.append(list(input().rstrip()))

graph_rg = deepcopy(graph)  # 적록색약인 사람(원본 배열을 유지하기위해 깊은 복사)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph_rg[i][j] = 'R'

visited = [[False] * n for _ in range(n)]


def bfs(x, y):
    q = deque([])
    q.append([x, y])
    visited[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])


# 적록색약이 아닌 경우
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1

# 적록색약인 경우
graph = graph_rg
visited = [[False] * n for _ in range(n)]  # 방문 배열 초기화
cnt_rg = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt_rg += 1

print(cnt, cnt_rg)
