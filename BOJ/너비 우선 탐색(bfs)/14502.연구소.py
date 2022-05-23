from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    global ans
    lab = deepcopy(graph)

    for x in range(n):
        for y in range(m):
            if lab[x][y] == 2:  # 바이러스일 때
                q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if lab[nx][ny] == 0:
                    q.append([nx, ny])
                    lab[nx][ny] = 2  # 바이러스 전파

    cnt = 0
    for line in lab:
        cnt += line.count(0)
    ans = max(ans, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                graph[x][y] = 1  # 벽 세움
                makeWall(cnt+1)
                graph[x][y] = 0  # 원상복귀


makeWall(0)
print(ans)
