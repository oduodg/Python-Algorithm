from collections import deque
import sys
input = sys.stdin.readline
row, col = map(int, input().split())
graph = [[] for _ in range(row)]
for i in range(row):
    graph[i] = list(map(int, input().split()))

time = 0
cheese = []

def bfs(x, y):
    cnt = 0
    visited = [[False for _ in range(col)] for _ in range(row)]
    q = deque([[x, y]])
    visited[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny + col:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 0:
                        q.append([nx, ny])
                    else:
                        graph[nx][ny] = 0
                        cnt += 1
    return cnt

while True:
    cnt = bfs(0, 0)
    if cnt == 0:
        break
    else:
        time += 1
        cheese.append(cnt)

print(time)
print(cheese[-1])
