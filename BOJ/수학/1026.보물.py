import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for _ in range(n):
    x = min(a)
    y = max(b)
    result += x * y
    a.remove(x)
    b.remove(y)

print(result)
