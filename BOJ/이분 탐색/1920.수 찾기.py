import sys
input = sys.stdin.readline # 입력 가속

n = int(input())
a = set(map(int, input().split()))
m = int(input())
targets = map(int, input().split())

for target in targets:
    if target in a:
        print(1)
    else:
        print(0)