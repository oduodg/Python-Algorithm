import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())  # 상자의 개수 n
box = list(map(int, input().split()))  # 상자들

# dp[i]는 i번째 상자에 넣을 수 있는 최대 상자 개수
dp = [1 for _ in range(n)]  # 자기 자신 1개씩
for i in range(1, n):  # 뒷 상자
    for j in range(0, i):  # 앞 상자
        if box[j] < box[i]:  # 앞 상자가 더 작으면
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
