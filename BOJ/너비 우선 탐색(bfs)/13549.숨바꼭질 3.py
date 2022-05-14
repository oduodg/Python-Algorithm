from collections import deque
n, k = map(int, input().split())


def valid(n):  # 유효한 위치인지 검사
    if n < 0 or n > 100000:
        return False
    return True


def solution(n, k):
    q = deque([[0, n]])
    visited = [False] * 100001

    while True:
        depth, x = q.popleft()
        visited[x] = True  # 방문 표시

        if x == k:
            return depth

        if valid(2*x) and not visited[2*x]:
            q.append([depth, 2*x])
            visited[2*x] = True

        depth += 1
        if valid(x-1) and not visited[x-1]:
            q.append([depth, x-1])
            visited[x-1] = True
        if valid(x+1) and not visited[x+1]:
            q.append([depth, x+1])
            visited[x+1] = True


print(solution(n, k))
