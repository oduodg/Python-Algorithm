from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[[] for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, list(input().rstrip())))


# 3차원 방문 배열(x, y, z): x, y는 위치 / z는 벽 부수고 나서 이동한 경로인지 여부
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

# print(graph)
# print(visited)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, flag):
    q = deque([[x, y, flag]])
    visited[x][y][flag] = 1

    while q:
        curr = q.popleft()
        x, y, flag = curr[0], curr[1], curr[2]

        if x == n-1 and y == m-1:
            return visited[x][y][flag]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 아니고 아직 방문하지 않은 경우
                if graph[nx][ny] == 0 and visited[nx][ny][flag] == 0:
                    visited[nx][ny][flag] = visited[x][y][flag] + 1
                    q.append([nx, ny, flag])
                
                # 벽이고 아직 한번도 안뚫은 경우 -> 벽 뚫기
                elif graph[nx][ny] == 1 and flag == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx, ny, 1])
    return -1

print(bfs(0, 0, 0))