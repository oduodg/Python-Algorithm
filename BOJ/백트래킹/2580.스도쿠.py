import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:  # 0인 값의
            blank.append([i, j])  # 위치를 저장한다.


def checkRow(row, val):  # 행 체크
    for i in range(9):
        if val == sudoku[row][i]:  # 값이 이미 행에 있는 경우
            return False
    return True


def checkCol(col, val):  # 열 체크
    for i in range(9):
        if val == sudoku[i][col]:  # 값이 이미 열에 있는 경우
            return False
    return True


def checkBox(row, col, val):
    left = (row//3) * 3  # 박스가 시작하는 행
    top = (col//3) * 3  # 박스가 시작하는 열

    for i in range(left, left+3):
        for j in range(top, top+3):
            if val == sudoku[i][j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit()

    x, y = blank[idx][0], blank[idx][1]
    for ans in range(1, 10):  # 답이 될 수 있는 값인 1~9 확인
        if checkRow(x, ans) and checkCol(y, ans) and checkBox(x, y, ans):  # 행, 열, 박스를 모두 확인해서 값이 맞으면
            sudoku[x][y] = ans  # 답을 적어줌
            dfs(idx+1)  # 그 다음 0의 값 확인
            sudoku[x][y] = 0  # 백트래킹 후 답이 맞지 않으면 다시 0으로 초기화


dfs(0)
