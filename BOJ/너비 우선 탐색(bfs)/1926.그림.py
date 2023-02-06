import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
painting = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(start_x, start_y):
	q = deque([[start_x, start_y]])
	visited[start_x][start_y] = True
	area = 1 # 그림의 넓이
	while q:
		x, y = q.popleft()
		dx = [0, 0, -1, 1]
		dy = [-1, 1, 0, 0]

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < m:
				if painting[nx][ny] and not visited[nx][ny]:
					q.append([nx, ny])
					visited[nx][ny] = True
					area += 1
	
	return area

count = 0
max_area = 0
for i in range(n):
	for j in range(m):
		if painting[i][j] and not visited[i][j]:
			max_area = max(max_area, bfs(i, j))
			count += 1

print(count)
if count: print(max_area)
else:	print(0)