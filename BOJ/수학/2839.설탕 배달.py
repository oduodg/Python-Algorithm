import sys
input = sys.stdin.readline # 입력 가속

N = int(input())

temp = []
# 3x + 5y = N, x가 작고 y가 클수록 좋음.

def sugar(N):
    for x in range(N):
        y = (N - 3*x) //5
        if (N - 3*x) /5 == y and y >= 0:
            return x+y
            break
    return -1

print(sugar(N))