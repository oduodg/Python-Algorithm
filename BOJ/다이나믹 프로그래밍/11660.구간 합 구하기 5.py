import sys
input = sys.stdin.readline  # 입력 가속
n, m = map(int, input().split())

# NxN 그래프 생성
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# 가로 + 세로 누적 합 dp 그래프 생성
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i-1][j-1] - dp[i-1][j-1]

# (x1,y1)부터 (x2, y2)까지의 합 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
