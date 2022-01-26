import sys
input = sys.stdin.readline # 입력 가속
c, k, p = map(int, input().split())
print(k*(c*(c+1)//2) + p*((c*(c+1)*(2*c+1))//6))