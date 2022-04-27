import sys
input = sys.stdin.readline
t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    n = int(input()) # 전화번호의 수
    phoneNumber = [0] * n
    for i in range(n):
        phoneNumber[i] = input().rstrip()
    phoneNumber.sort()
    for i in range(n-1):
        if phoneNumber[i+1].startswith(phoneNumber[i]):
            print('NO')
            break
        else:
            if i == n-2:
                print('YES')