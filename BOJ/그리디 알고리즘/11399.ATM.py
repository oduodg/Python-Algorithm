import sys
input = sys.stdin.readline # 입력 가속
n = int(input()) # 사람의 수
time = sorted(list(map(int, input().split()))) # 걸리는 시간
min_time = 0
for i in range(1, n+1):
    min_time += sum(time[:i])

print(min_time)