import sys
input = sys.stdin.readline  # 입력 가속

# 입력받기
n, k = map(int, input().split())  # 물품의 수 n, 버틸 수 있는 무게 k
items = [[0, 0]] * (n+1)  # n개의 물건들의 [무게, 가치]

for i in range(1, n+1):
    items[i] = list(map(int, input().split()))

# 0-1 배낭 알고리즘
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]  # dp 배열 초기화

for i in range(1, n+1):
    for j in range(1, k+1):
        w = items[i][0]  # i번째 물건의 무게
        v = items[i][1]  # i번째 물건의 가치
        if w <= j:  # 물건을 가방에 넣을 수 있는 경우
            # 물건을 넣지않을 때, 넣었을 때 중 큰 값
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
        else:  # 물건이 무거워서 가방에 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]  # 물건을 넣지않았을 때의 값

print(dp[n][k])
