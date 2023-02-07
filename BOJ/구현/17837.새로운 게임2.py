import sys
input = sys.stdin.readline
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse = []
letters = [chr(i) for i in range(65, 75)] # 4 <= K <= 10 이므로 "A"부터 "J" 까지의 말
for _ in range(k):
	x, y, d = map(int, input().split())
	horse.append([x-1, y-1, d-1])
chess = dict(zip(letters, horse)) # (ex) "A": [x, y, d]
location = [[[] for _ in range(n)] for _ in range(n)]
for horse in chess:
	x, y, d = chess[horse]
	location[x][y].append(horse)

def change_direction(d):
	if d in [0, 2]: return d+1
	if d in [1, 3]: return d-1

def next_square(x, y, d):
	# right, left, up, down
	dx = [0, 0, -1, 1]
	dy = [1, -1, 0, 0]
	return x + dx[d], y + dy[d]

def is_within_range(x, y):
	if 0 <= x < n and 0 <= y < n:	return True
	else: return False
	
def move(horse):
	x, y, d = chess[horse]
	nx, ny = next_square(x, y, d)
	my_idx = location[x][y].index(horse)
	
	# 체스판을 벗어나거나 다음 칸이 파란색인 경우
	if not is_within_range(nx, ny) or board[nx][ny] == 2: 
		d = change_direction(d)
		chess[horse] = [x, y, d]
		nx, ny = next_square(x, y, d)
		if not is_within_range(nx, ny) or board[nx][ny] == 2: 
			return False

	horse_up = location[x][y][my_idx:]
	for horse in horse_up:
		chess[horse][0], chess[horse][1] = nx, ny
	# 다음 칸이 흰색인 경우
	if board[nx][ny] == 0: 
		location[nx][ny].extend(horse_up)
	# 다음 칸이 빨간색인 경우
	if board[nx][ny] == 1: 
		location[nx][ny].extend(list(reversed(horse_up)))
	location[x][y] = location[x][y][:my_idx]
	if len(location[nx][ny]) >= 4:
		return True
	return False

turn = 1
while turn < 1000:
	for horse in chess:
		if move(horse):
			print(turn)
			sys.exit()
	turn += 1

print(-1)