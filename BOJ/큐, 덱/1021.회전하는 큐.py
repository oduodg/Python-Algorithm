import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
idxs = list(map(int, input().split()))

d = [i for i in range(1, n+1)]
d = deque(d)

cnt = 0  # 연산 횟수 카운트

for idx in idxs:
    if idx == d[0]:
        d.popleft()  # 첫 번째 원소 뽑아냄
        continue

    if d.index(idx) <= (len(d)//2):  # 앞에서 더 가까우면
        while idx != d[0]:
            d.append(d.popleft())  # 왼쪽으로 한 칸 이동
            cnt += 1  # 연산 횟수 증가
        d.popleft()
        continue
    else:  # 뒤에서 더 가까우면
        while idx != d[0]:
            d.appendleft(d.pop())  # 오른쪽으로 한 칸 이동
            cnt += 1
        d.popleft()
        continue

print(cnt)
