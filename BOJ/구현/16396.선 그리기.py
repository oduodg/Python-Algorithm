import sys
input = sys.stdin.readline
n = int(input())
line = [False] * 10001
for _ in range(n):
    x, y = map(int, input().split())
    for num in range(x, y):
        line[num] = True

print(line.count(True))