import sys
input = sys.stdin.readline # 입력 가속
t = int(input()) # test case의 개수
for _ in range(t):
    a, b = map(int, input().split())
    # 시간초과를 해결하기 위해 "밑수의 일의 자리 규칙"을 활용해야 함
    base = a % 10 # 밑수
    if base == 0:
        print(10)
    elif base in [1, 5, 6]:
        print(base)
    elif base in [2, 3, 7, 8]:
        if b % 4 == 1:
            print(base)
        elif b % 4 == 0:
            print((base**4)%10)
        else:
            print((base**(b%4))%10)
    else: # base = 4, 9 일 때
        if b % 2 == 1:
            print(base)
        else:
            print((base**2)%10)