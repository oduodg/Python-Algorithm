import sys
input = sys.stdin.readline

n = int(input())
board = [0] * n  # 인덱스는 가로(행), 값은 세로(열)을 나타냄
cnt = 0  # 경우의 수


def adj(x):  # 인접한 칸인지 확인
    for j in range(x):  # x 이전까지 검사(먼저 배치한 퀸들의 대각선을 확인)
        # 세로(값이 같으면 같은 열), 대각선 검사("행 차이 = 열 차이"이면 같은 대각선 )
        if board[j] == board[x] or x - j == abs(board[x] - board[j]):
            return False
    return True


def dfs(x):
    global cnt
    if x == n:  # n개의 퀸을 배치하면
        cnt += 1  # 경우의 수 +1
        return

    for i in range(n):
        board[x] = i
        if adj(x):  # 행, 열, 대각선 체크
            dfs(x+1)  # 다음 퀸 위치 찾기


dfs(0)
print(cnt)
