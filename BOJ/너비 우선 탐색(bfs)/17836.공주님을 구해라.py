from collections import deque
import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
graph = [[[] for _ in range(m)] for _ in range(n)]
for i in range(n):
	graph[i] = list(map(int, input().split()))

visited = [[False for _ in range(m)] for _ in range(n)]
time = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sword = 0
def bfs(x, y):
	q = deque([[x, y]])
	visited[x][y] = True
	global sword

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
				visited[nx][ny] = True
				time[nx][ny] = time[x][y] + 1
				if graph[nx][ny] == 2: # 검을 찾음
					d = (n-1) - nx + (m-1) - ny
					sword = time[nx][ny] + d

				elif graph[nx][ny] == 0:
					q.append([nx, ny])
				

bfs(0, 0)
if time[n-1][m-1] != 0 and sword != 0:
	res = min(time[n-1][m-1], sword)
elif time[n-1][m-1] == 0 and sword == 0:
	res = 0
else: # 둘 중에 하나가 0
	res = max(time[n-1][m-1], sword)


if res > t or res == 0:
	print("Fail")
else:
	print(res)