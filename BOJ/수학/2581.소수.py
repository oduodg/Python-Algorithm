import sys
input = sys.stdin.readline # 입력 가속

M = int(input())
N = int(input())

num = set(range(2, N+1))
for i in range(2, N+1):
    if i in num:
        num -= set(range(i*2, N+1, i))
        
num -= set(range(1, M))

if len(num) < 1:
    print(-1)
else:
    print(sum(num)) # 소수들의 합
    print(min(num)) # 소수들 중 최솟값