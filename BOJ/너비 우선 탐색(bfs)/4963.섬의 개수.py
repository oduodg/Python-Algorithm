from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True

    while q:
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        dx = [0, 0, -1, 1, -1, -1, 1, 1]
        dy = [-1, 1, 0, 0, -1, 1, -1, 1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = True


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        line = list(map(int, input().split()))
        graph.append(line)

    visited = [[False]*w for _ in range(h)]
    land = 0
    for x in range(h):
        for y in range(w):
            if not visited[x][y] and graph[x][y] == 1:
                bfs(x, y)
                land += 1
    print(land)
