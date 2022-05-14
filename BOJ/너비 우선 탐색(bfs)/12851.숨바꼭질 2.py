import sys
from collections import deque
n, k = map(int, input().split())


def valid_location(n):
    if n < 0 or n > 100000:
        return False
    return True


def solution(n, k):
    depth, location = 0, n
    q = deque([[depth, location]])
    visited = [False] * 100001  # 방문한 위치 표시 배열
    cnt = 0
    time = sys.maxsize
    while q:
        depth, x = q.popleft()  # 트리의 깊이, 위치 x
        visited[x] = True

        if x == k:
            time = depth
            cnt += 1

        if cnt > 0 and depth > time:
            return time, cnt

        depth += 1
        if valid_location(x-1):
            if not visited[x-1]:
                q.append([depth, x-1])
        if valid_location(x+1):
            if not visited[x+1]:
                q.append([depth, x+1])
        if valid_location(2*x):
            if not visited[2*x]:
                q.append([depth, 2*x])

    return time, cnt


time, cnt = solution(n, k)
print(time)
print(cnt)
