from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
answer = []
""" # 시간 초과
cnt = 0
while len(answer) < n:
    for i in range(1, n+1):
        cnt += 1
        if i in answer:
            cnt -= 1
        if cnt == k:
            answer.append(i)
            cnt = 0
print('<' + ', '.join(map(str, answer)) + '>')
"""
q = deque([i for i in range(1, n+1)])
while q:
    for i in range(k-1):
        q.append(q.popleft())  # k번째 이전 사람들은 다시 맨 뒤로
    answer.append(q.popleft())  # k번째 사람
print('<' + ', '.join(map(str, answer)) + '>')
