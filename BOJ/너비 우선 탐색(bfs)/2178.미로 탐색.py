import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maze = []
for _ in range(n):
    line = list(input().rstrip())
    line = list(map(int, line))
    maze.append(line)

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
q = deque([[0, 0]])  # 출발 지점 삽입


def bfs(x, y):
    # 상하좌우 탐색
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < n and 0 <= Y < m:
            if maze[X][Y] == 1:
                q.append([X, Y])
                maze[X][Y] = maze[x][y] + 1


while q:
    curr = q.popleft()
    x, y = curr[0], curr[1]
    bfs(x, y)

print(maze[n-1][m-1])
