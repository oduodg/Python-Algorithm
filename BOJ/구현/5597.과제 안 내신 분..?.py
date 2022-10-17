import sys
input = sys.stdin.readline
chk = [False] * 31
ans = []

for _ in range(28):
	chk[int(input())] = True

for i in range(1, 31):
	if chk[i] == False:
		ans.append(i)

ans.sort()
print(ans[0])
print(ans[1])