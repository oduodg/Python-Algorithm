import sys
from collections import deque
input = sys.stdin.readline  # 입력 가속

t = int(input())  # 테스트 케이스의 수
for _ in range(t):
    p = input()  # 수행할 함수
    n = int(input())  # 배열에 들어있는 수의 개수
    arr = input().rstrip()[1:-1].split(',')
    dq = deque(arr)

    r_flag = False  # 뒤집기 플래그
    error = False  # 에러 플래그

    if n == 0:  # 배열이 비었을 때
        dq = deque([])

    for i in range(len(p)):
        if p[i] == 'R':
            if r_flag:
                r_flag = False
            else:
                r_flag = True
        elif p[i] == 'D':
            if not dq:
                error = True
                break
            if r_flag:  # 뒤집어졌으면
                dq.pop()  # 오른쪽 끝 버리기
            else:  # 뒤집어지지 않았으면
                dq.popleft()  # 맨 처음 버리기
    if not error:
        if r_flag:
            dq.reverse()
            print('[' + ','.join(dq) + ']')
        else:
            print('[' + ','.join(dq) + ']')
    else:
        print('error')
