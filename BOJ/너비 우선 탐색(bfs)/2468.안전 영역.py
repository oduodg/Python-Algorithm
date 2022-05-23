from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = []
low = 100
high = 1
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    low = min(min(line), low)
    high = max(max(line), high)


def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True

    while q:
        curr = q.popleft()
        x = curr[0]
        y = curr[1]

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > rain:
                    q.append([nx, ny])
                    visited[nx][ny] = True


ans = 1
for rain in range(low, high):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > rain:
                bfs(i, j)
                cnt += 1

    ans = max(ans, cnt)

print(ans)
