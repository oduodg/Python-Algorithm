from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
q = deque([])

for i in range(n):
    box.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if box[x][y] == 1:  # 익은 토마토이면
            q.append([x, y])  # 큐에 넣어줌


def bfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:  # 토마토가 익지 않았으면
                q.append([nx, ny])  # 큐에 추가
                box[nx][ny] = box[x][y] + 1  # 토마토가 익은 날짜 증가


while q:
    x, y = q.popleft()
    bfs(x, y)

ans = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:  # 안 익은 토마토가 있으면
            print(-1)
            exit(0)  # 종료
    ans = max(ans, max(box[i]))
print(ans-1)
