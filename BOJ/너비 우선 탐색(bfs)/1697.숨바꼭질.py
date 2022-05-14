from collections import deque
n, k = map(int, input().split())


def valid_location(n):
    if n < 0 or n > 100000:
        return False
    return True


def solution(n, k):
    location = [0, n]
    q = deque([location])
    visited = [False] * 100001  # 방문한 위치 표시 배열

    while True:  # k에 도착할 때까지
        depth, x = q.popleft()  # 트리의 깊이, 위치 x
        visited[x] = True
        if x == k:
            return depth

        next = [x-1, x+1, 2*x]
        depth += 1
        if k in next:
            return depth

        if valid_location(x-1) and not visited[x-1]:
            q.append([depth, x-1])
        if valid_location(x+1) and not visited[x+1]:
            q.append([depth, x+1])
        if valid_location(2*x) and not visited[2*x]:
            q.append([depth, 2*x])


print(solution(n, k))
