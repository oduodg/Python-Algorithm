import sys
input = sys.stdin.readline # 입력 가속
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)] # 2차원 배열 dp
# dp[x][y] : x번째 자리 수에 숫자 y가 올 수 있는 경우의 수
# dp[n]의 합을 1,000,000,000 으로 나눈 나머지가 정답이 된다.
dp[1] =[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n+1): # 2부터 n까지
    for j in range(0,10): # 0부터 9까지
        if j == 0: # 앞자리 수가 0인 경우 다음 숫자는 1만 올 수 있다.
            dp[i][j] = dp[i-1][1]
        elif j == 9: # 앞자리 수가 9인 경우 다음 숫자는 8만 올 수 있다.
            dp[i][j] = dp[i-1][8]
        else: # 앞자리 수가 2~8인 경우는 자기 자신 -1, 자기 자신 +1 인 숫자 2가지가 올 수 있다.
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n])%1000000000)