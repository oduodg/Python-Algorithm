import sys
input = sys.stdin.readline
n = int(input())
arr = [-1] * 11
ans = 0
for i in range(n):
	num, location = map(int, input().split())
	if arr[num] == -1:
		arr[num] = location
	else:
		if arr[num] != location:
			arr[num] = location
			ans += 1

print(ans)