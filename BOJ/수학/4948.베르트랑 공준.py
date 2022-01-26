import sys
for n in map(int, sys.stdin): # 여러 개의 입력
    if n == 0:
        break
    num = set(range(2, 2*n+1)) # 2부터 2n까지의 숫자들
    for i in range(2, 2*n+1):
        if i in num:
            num -= set(range(i*2, 2*n+1, i)) # i의 배수들을 제거
    num -= set(range(2, n+1)) # n까지의 숫자들 제거
    print(len(num))