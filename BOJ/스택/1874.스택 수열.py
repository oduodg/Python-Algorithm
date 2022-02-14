import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())  # 수의 개수
stack = []
cur = 1
flag = True
answer = []
for _ in range(n):
    num = int(input())

    while cur <= num:
        stack.append(cur)
        cur += 1
        answer.append('+')

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = False

if not flag:
    print('NO')
else:
    for op in answer:
        print(op)
