import sys
input = sys.stdin.readline
a = int(input()) # 사람 a명
t = int(input()) # t번째
x = int(input()) # 0이면 뻔, 1이면 데기

cnt = 0 # cnt번째 "뻔" or "데기"
n = 1 # n번째 라운드
total = 0 # 총 횟수

while True:
	round = [0, 1, 0, 1] + [0] * (n+1) + [1] * (n+1)
	for i in range(len(round)):
		# 카운트하기
		if round[i] == x:
			cnt += 1

		if cnt == t: # t번째 사람
			idx = total + i # 인덱스
			print(idx%a) # 사람 수로 나눈 나머지가 답
			sys.exit()

  # 다음 라운드로
	total += len(round)
	n += 1