import sys
input = sys.stdin.readline # 입력 가속

x, y, w, h = map(int, input().split())

print(min((w-x), (h-y), x, y))