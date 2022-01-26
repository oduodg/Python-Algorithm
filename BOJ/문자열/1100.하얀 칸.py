import sys
input = sys.stdin.readline # 입력 가속
line, cnt = 0, 0
for _ in range(8):
    line += 1
    chess = input()
    if line % 2 == 1:
        for i in range(0,8,2):
            if chess[i] == 'F':
                cnt += 1
    else:
        for i in range(1,8,2):
            if chess[i] == 'F':
                cnt += 1
print(cnt)