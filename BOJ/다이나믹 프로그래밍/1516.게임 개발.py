import sys
input = sys.stdin.readline
n = int(input()) # 건물의 종류 수
building = [[]] # 건물 정보
dp = [0] * (n+1) # dp[i]: i번째 건물 짓는데 걸리는 시간
for _ in range(n):
    temp = list(map(int, input().split()))
    building.append(temp)

# 먼저 지어져야 할 건물이 없는 경우
for i in range(1, n+1):
    if len(building[i]) == 2:
        dp[i] = building[i][0]

def dfs(i):
    if dp[i]:
        return dp[i]

    max_time = 0
    for x in range(1, len(building[i])-1):
        time = dfs(building[i][x])
        max_time = max(time, max_time) # 먼저 지어야할 건물 중 짓는데 가장 오래 걸리는 시간
    
    dp[i] = max_time + building[i][0]
    return dp[i]

for i in range(1, n+1):
    print(dfs(i))

# Test case
'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

10
20
14
18
17
--------------
3
10 2 -1
10 3 -1
10 -1

30
20
10
--------------
4
10 2 -1
10 3 -1
10 4 -1
10 -1

40
30
20
10
--------------
6
10 -1
10 1 6 -1
4 1 -1
4 3 1 -1
3 3 -1
9 -1

10
20
14
18
17
9
--------------
5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1

10
30
60
140
100
--------------
5
10 2 -1
10 3 5 4 -1
10 4 -1
10 5 -1
10 -1

50
40
30
20
10
--------------
'''