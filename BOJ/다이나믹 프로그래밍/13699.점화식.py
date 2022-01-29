import sys
input = sys.stdin.readline # 입력 가속
t = [1] + [0] * 35 # 0 <= n <= 35
n = int(input())
for i in range(1, n+1):
    for j in range(0, i):
        t[i] += t[j] * t[i-j-1]
print(t[n])