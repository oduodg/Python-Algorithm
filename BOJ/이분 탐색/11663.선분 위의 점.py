import sys
input = sys.stdin.readline
n, m = map(int, input().split())
point = list(map(int, input().split()))
point.sort()

def binarySearch(target):
	l, r = 0, n-1
	while l <= r:
		mid = (l+r)//2
		if point[mid] < target:
			l = mid + 1
		elif point[mid] > target:
			r = mid - 1
		else:
			return [mid, mid]
	return [l, r]

def solution(start, end):
	return binarySearch(end)[1] - binarySearch(start)[0] + 1
	
for i in range(m):
	start, end = map(int, input().split())
	print(solution(start, end))