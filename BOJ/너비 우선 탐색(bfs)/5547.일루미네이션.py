from collections import deque
import sys
input = sys.stdin.readline
w, h = map(int, input().split()) # 가로 w, 세로 h
graph = [[] for _ in range(h+2)]
# 위 아래 한 줄씩 총 2줄 더 추가
graph[0] = [0 for _ in range(w+2)]
graph[h+1] = [0 for _ in range(w+2)]
for i in range(1, h+1):
    # 양 옆으로 0을 추가해줌 (양 옆으로 세로 한 줄씩 총 2줄 더 추가)
    graph[i] = [0] + list(map(int, input().split())) + [0]


visited = [[False for _ in range(w+2)] for _ in range(h+2)]

# 짝수행: 상하좌우 + 좌상/좌하, 홀수행: 상하좌우 + 우상/우하
even_row, odd_row = [0, 0, -1, 1, -1, -1], [0, 0, -1, 1, 1, 1]
col = [1, -1, 0, 0, 1, -1]

def bfs(x, y):
    ans = 0
    q = deque([[x, y]])
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + col[i]
            if x % 2 == 0: # 짝수행
                ny = y + even_row[i]
            else: # 홀수행
                ny = y + odd_row[i]
            
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if graph[nx][ny] == 1:
                    ans += 1
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny])
    return ans

print(bfs(0, 0))