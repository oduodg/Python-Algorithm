import sys
a, b, c, m = map(int, input().split())
if a > m:
	print(0)
	sys.exit(0)

burn = 0 # 현재 피로도
work = 0 # 일 처리량
for i in range(24):
	# 일할 수 있다면
	if (m-burn) >= a: 
		work += b # b만큼 일 처리
		burn += a # a만큼 피로도 축적
	
	# 일할 수 없다면 -> 휴식
	else:
		burn -= c
		if burn < 0: burn = 0 # 피로도는 음수가 될 수 없음

print(work)