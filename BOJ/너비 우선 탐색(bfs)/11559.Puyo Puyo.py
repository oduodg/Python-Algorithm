from collections import deque
import sys
input = sys.stdin.readline
row = 12
col = 6
field = []
for _ in range(row):
    field.append(list(input().rstrip()))

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    # 상하좌우 탐색
    for d in range(4):
        X = x + dx[d]
        Y = y + dy[d]
        if 0 <= X < row and 0 <= Y < col:
            # 같은 색이고, 방문한 적이 없으면
            if field[X][Y] == field[x][y] and not visited[X][Y]:
                q.append([X, Y])  # 큐에 저장
                visited[X][Y] = True  # 방문 기록


def down():  # 뿌요 떨어트리기
    for y in range(col):  # 열 단위로 진행
        bag = deque([])  # 뿌요 순서를 담을 큐
        for x in range(11, -1, -1):  # 아래서 위로 올라가면서(아래에 있는 것이 먼저 떨어지니까 큐를 활용하기 위해서 아래서부터 담아준다.)
            if field[x][y] != '.':  # 뿌요가 있으면
                bag.append(field[x][y])  # 큐에 넣음
        for x in range(11, -1, -1):
            if bag:  # 가방에 뿌요가 있으면
                field[x][y] = bag.popleft()  # 뿌요를 떨어트림
            else:  # 가방이 비면
                field[x][y] = '.'  # 뿌요가 없음


check = False  # 뿌요 터짐 체크
ans = 0  # 총 연쇄 횟수
while True:
    # 방문 확인 배열(뿌요가 터질 때 마다 새로 방문 확인해주어야 함)
    visited = [[False]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            # 뿌요가 있고, 방문한 적이 없으면
            if field[i][j] != '.' and not visited[i][j]:
                q = deque([[i, j]])  # 큐에 넣음
                visited[i][j] = True  # 방문 표시
                location = []  # 뿌요의 위치를 기록할 배열
                while q:
                    curr = q.popleft()  # 큐에서 꺼냄
                    location.append(curr)  # 위치 기록
                    bfs(curr[0], curr[1])  # 상하좌우 탐색

                    if len(location) >= 4:  # 이어진 뿌요가 4개 이상이면
                        check = True
                        for puyo in location:
                            field[puyo[0]][puyo[1]] = '.'  # 뿌요 터짐

    if not check:  # 터진 뿌요가 없다면
        break  # while문 종료

    down()  # 뿌요 떨어짐
    check = False  # False로 초기화
    ans += 1  # 연쇄 횟수 증가

print(ans)
