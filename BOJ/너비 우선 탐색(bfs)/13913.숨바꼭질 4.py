from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
visited = [False] * 100001  # 방문 표시 배열
check = [0] * 100001  # 노드 이동 정보: check[현재 위치] = 이전 위치


def valid(n):  # 유효한 위치인지 검사
    if n < 0 or n > 100000:
        return False
    return True


def move(sec, now):
    route = deque([now])  # 경로를 담을 배열
    x = now
    for _ in range(sec):
        route.appendleft(check[x])
        x = check[x]  # 이전 위치
    return list(route)


def solution(n, k):
    q = deque([[0, n]])
    visited[n] = True  # 방문
    while q:
        sec, now = q.popleft()  # 큐에서 꺼냄

        if now == k:  # 동생을 만나면
            return sec, move(sec, now)

        for next in (now-1, now+1, 2*now):
            if valid(next) and not visited[next]:
                q.append([sec+1, next])  # 큐에 추가
                visited[next] = True  # 방문
                check[next] = now  # 다음 위치에 현재(지나가는 위치) 위치를 기록


sec, route = solution(n, k)
print(sec)
print(*route)
