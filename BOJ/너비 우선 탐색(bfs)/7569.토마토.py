from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
box = [[[[] for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        line = list(map(int, input().split()))
        box[i][j] = line
        for k in range(m):
            if box[i][j][k] == 1:  # 익은 토미토이면
                q.append([i, j, k])  # 큐에 넣어준다.

ans = 0
while q:
    z, y, x = q.popleft()

    # 위,아래, 앞, 뒤, 왼쪽, 오른쪽
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dx = [0, 0, 0, 0, -1, 1]

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if box[nz][ny][nx] == 0:  # 익지 않은 토마토가 있으면
                q.append([nz, ny, nx])  # 큐에 넣어준다.
                box[nz][ny][nx] = box[z][y][x] + 1  # 익은 날짜수 증가
            ans = max(ans, box[nz][ny][nx])  # 익는데 가장 오래걸린 날짜수를 저장

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:  # 익지 않은 토마토가 있다면
                print(-1)
                exit(0)  # 종료

print(ans-1)  # 맨 처음 익은 토마토가 1부터 시작했으므로 -1을 해준다.
