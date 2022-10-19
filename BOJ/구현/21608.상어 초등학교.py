import sys
input = sys.stdin.readline
n = int(input())
arr = [0 for _ in range(n*n +1)] # 학생 순서를 담을 배열
like = [[] for _ in range(n*n +1)] # 좋아하는 학생 담을 배열(인덱스는 자신의 번호)
#chk = [False for _ in range(n*n +1)] # 자리를 정했는지 여부
#seat = [[] for _ in range(n*n +1)] # 정해진 자리를 담을 배열(인덱스는 자신의 번호)
classroom = [[0]*(n+1) for _ in range(n+1)] # 자리

for i in range(1, n*n+1):
	user_input = list(map(int, input().split()))
	arr[i] = user_input[0]
	like[arr[i]] = user_input[1:]

def take_a_seat(student_num):
	seat = [] # 앉을 수 있는 칸의 위치를 담을 배열
	score1 = [] # 인접한 칸에 있는 좋아하는 학생의 수를 담을 배열(1번 조건)
	score2 = [] # 인접한 칸 중 비어있는 칸의 수를 담을 배열(2번 조건)
	for i in range(1, n+1):
		for j in range(1, n+1):
			curr_score1 = 0 # 인접한 칸에 있는 좋아하는 학생의 수
			curr_score2 = 0 # 인접한 칸 중 비어있는 칸의 수

			# 비어있는 칸 중에서
			if classroom[i][j] == 0:
				seat.append([i, j])

				# 인접한 칸 찾기 -> 자리를 기준으로 동서남북이 인접한 칸
				dx = [0, 0, 1, -1]
				dy = [1, -1, 0, 0]
				for k in range(4):
					curr_x = i + dx[k]
					curr_y = j + dy[k]
					# 앉을 수 있는 자리인지 범위 체크
					if 1 <= curr_x <= n and 1 <= curr_y <= n:	
						# 인접한 자리에 좋아하는 학생이 있다면(1번 조건)
						if classroom[curr_x][curr_y] in like[student_num]:
							curr_score1 += 1
						
						# 인접한 자리가 비어있다면(2번 조건)
						if classroom[curr_x][curr_y] == 0:
							curr_score2 += 1
				
				score1.append(curr_score1)
				score2.append(curr_score2)

	max_score1 = max(score1)
	idx_list1 = [i for i,v in enumerate(score1) if v == max_score1]
	
	# 1번 조건을 만족하는 칸이 여러개인 경우 -> 2번 조건
	if len(idx_list1) >= 2:
		max_score2 = 0
		for i in range(len(idx_list1)):
			max_score2 = max(score2[idx_list1[i]], max_score2)

		idx_list2 = []
		for i in range(len(idx_list1)):
			if score2[idx_list1[i]] == max_score2:
				idx_list2.append(idx_list1[i])
		
		# 2번 조건을 만족하는 칸이 여러개인 경우 -> 3번 조건
		if len(idx_list2) >=2:
			idx_list3 = []
			for i in range(len(idx_list2)):
				idx_list3.append(idx_list2[i])

			last = []
			for i in range(len(idx_list3)):
				last.append(seat[idx_list3[i]])
			last.sort(key=lambda x:(x[0], x[1]))
			my_seat_x, my_seat_y = last[0][0], last[0][1]

		# 2번 조건을 만족하는 칸이 1개인 경우
		else:
			my_seat_x, my_seat_y = seat[idx_list2[0]][0], seat[idx_list2[0]][1]
	
	# 1번 조건을 만족하는 칸이 1개인 경우
	else:
		my_seat_x, my_seat_y = seat[idx_list1[0]][0], seat[idx_list1[0]][1]

	# 정해진 자리
	classroom[my_seat_x][my_seat_y] = student_num

def satisfy(my_seat_x, my_seat_y):
	cnt = 0 # 인접한 칸에 앉은 좋아하는 학생의 수
	# 인접한 칸 찾기 -> 자리를 기준으로 동서남북이 인접한 칸
	dx = [0, 0, 1, -1]
	dy = [1, -1, 0, 0]
	for k in range(4):
		curr_x = my_seat_x + dx[k]
		curr_y = my_seat_y + dy[k]
		if 1 <= curr_x <= n and 1 <= curr_y <= n:
			# 인접한 자리에 좋아하는 학생이 있다면
			if classroom[curr_x][curr_y] in like[classroom[my_seat_x][my_seat_y]]:
				cnt += 1

	# 만족도 구하기
	if cnt == 0:
		return 0
	elif cnt == 1:
		return 1
	elif cnt == 2:
		return 10
	elif cnt == 3:
		return 100
	else:
		return 1000

for i in range(1, n*n +1):
	take_a_seat(arr[i])

ans = 0 # 학생의 만족도의 총 합
for i in range(1, n+1):
	for j in range(1, n+1):
		ans += satisfy(i, j)

print(ans)