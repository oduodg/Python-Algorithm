import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split()) # 회원의 수, 치킨 종류의 수
p = [[] for _ in range(n)] # 각 회원의 치킨 선호도
for i in range(n):
	p[i] = list(map(int, input().split()))

ans = 0
for a, b, c in combinations(range(m), 3): # 치킨 3종류의 조합
	like = 0 # 만족도
	for i in range(n): # 모든 회원의 만족도를 더함
		like += max(p[i][a], p[i][b], p[i][c])
	ans = max(ans, like)
print(ans)