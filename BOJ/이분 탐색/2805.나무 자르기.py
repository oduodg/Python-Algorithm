import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 나무의 수, 나무의 길이
h = list(map(int, input().split())) # 나무의 높이

l, r = 0, max(h)
ans = 0
while l <= r:
	mid = (l+r)//2
	#print("l:", l, "mid:", mid, "r:", r)
	tree = 0
	for i in range(n):
		if h[i] <= mid:
			continue
		else:
			tree += h[i] - mid

	#print("tree:", tree, "m:", m)
	if tree == m: # 정확히 M미터의 나무를 가져갈 수 있는 경우
		ans = mid
		break
	elif tree > m:
		l = mid +1
		ans = max(ans, mid) # 정확히 M미터의 나무를 가져갈 수 없는 경우를 대비한다. -> 적어도 M미터의 나무를 가져가야하기 때문에
	else:
		r = mid -1

print(ans)

