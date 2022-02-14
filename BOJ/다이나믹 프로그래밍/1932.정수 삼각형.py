import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())  # 삼각형의 크기
dp = [0] * n
for i in range(n):
    dp[i] = list(map(int, input().split()))
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == len(dp[i])-1:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1]))
