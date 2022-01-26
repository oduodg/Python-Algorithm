import sys
input = sys.stdin.readline # 입력 가속
n = int(input()) # 진짜 약수의 개수
divisor = list(map(int, input().split())) # 진짜 약수
print(max(divisor) * min(divisor))