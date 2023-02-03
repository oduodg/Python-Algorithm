import sys
from collections import deque

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
result = []

def bfs(i, j):
    count = 1
    q = deque([[i, j]])
    visited[i][j] = True
    while q:
        dx = [0, 0, -1 ,1]
        dy = [1, -1, 0, 0]

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    count += 1
    
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()

print(len(result))
for count in result:
    print(count)