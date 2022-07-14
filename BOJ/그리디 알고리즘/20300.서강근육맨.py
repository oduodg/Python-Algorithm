from collections import deque # 덱
import sys
input = sys.stdin.readline

n = int(input()) # 운동기구의 개수
lose = list(map(int, input().split())) # 각 운동기구의 근손실 정도
m = 0

lose.sort() # 오름차순 정렬
lose = deque(lose)

if n % 2 == 1: # 홀수개인 경우
    m = lose.pop()

while lose:
    m = max(lose.popleft() + lose.pop(), m)

print(m)