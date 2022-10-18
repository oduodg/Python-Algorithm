import sys
input = sys.stdin.readline
n = int(input()) # 지방의 수
arr = list(map(int, input().split())) # 예산 요청
m = int(input()) # 총 예산

# 상한액이 될 수 있는 범위는 0 ~ max(arr)
# 위 범위에서 상한액을 찾아보자.
# 이분탐색 => 정렬
arr.sort()
l, r = 0, max(arr)
while l <= r:
	mid = (l+r)//2 # 상한액
	curr = m # 남은 예산
	for i in arr:
		if i <= mid: # 요청 예산이 상한액보다 작거나 같으면
			curr -= i # 요청 예산만큼 빼준다.
		else: # 요청 예산이 상한액보다 크면
			curr -= mid # 상한액만큼 빼준다.
	
	if curr >= 0: # 예산이 남으면
		l = mid + 1
	else: # 예산이 초과하면
		r = mid - 1

print(r)