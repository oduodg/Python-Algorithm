import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())
a = list(map(int, input().split()))
p = [0] * n
cnt = 0
while cnt < n:
    order = min(a)
    for i in range(n):
        if a[i] == order:
            p[i] = cnt
            cnt += 1
            a[i] = 1001
            break
for num in p:
    print(num, end=' ')
