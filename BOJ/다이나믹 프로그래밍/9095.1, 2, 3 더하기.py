import sys
input = sys.stdin.readline # 입력 가속

t = int(input()) # 테스트 케이스의 개수
dp = [0,1,2,4] + [0] * 7 # n은 11보다 작은 양수
for _ in range(t):
    n = int(input())
    if n in [1,2,3]:
        print(dp[n])
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])