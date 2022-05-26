import sys
input = sys.stdin.readline
r, c = map(int, input().split())  # 행, 열
board = [list(input().rstrip()) for _ in range(r)]
visited = set()
ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, cnt+1)
            visited.remove(board[nx][ny])


visited.add(board[0][0])
dfs(0, 0, 1)  # 좌측 상단에서 시작
print(ans)
