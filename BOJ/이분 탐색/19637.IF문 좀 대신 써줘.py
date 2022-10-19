import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 칭호의 개수 n, 캐릭터들의 개수 m
title = [[0, 0] for row in range(n)] # 칭호를 저장할 배열

# 칭호는 비내림차순으로 주어진다.
for i in range(n):
	title[i][0], title[i][1] = input().split()
	title[i][1] = int(title[i][1])

# 전투력 측정
def power_title(power):
	l, r = 0, n
	while l <= r:
		mid = (l+r)//2
		if power <= title[mid][1]:
			r = mid -1
		else:
			l = mid +1
	return title[l][0]

for i in range(m):
	print(power_title(int(input())))