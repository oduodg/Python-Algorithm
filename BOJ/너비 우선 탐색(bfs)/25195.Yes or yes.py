from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
s = int(input())  # 팬클럽 곰곰이가 존재하는 정점의 개수
fan = list(map(int, input().split()))  # 팬클럽 곰곰이가 존재하는 정점들

if 1 in fan:  # 출발지인 1번 노드에 팬클럽 곰곰이가 있다면
    print('Yes')
    exit(0)  # 종료

q = deque([1])  # 출발 노드
visited = [False, True] + [False] * (n-1)  # 방문 표시 배열

while q:
    curr = q.popleft()
    if not graph[curr]:  # 더 이상 이동할 수 없는 경우
        print('yes')
        exit(0)  # 종료
    for next in graph[curr]:  # 인접 정점들 중
        if next not in fan and not visited[next]:  # 팬클럽 곰곰이가 없고, 방문하지 않은 정점이면
            q.append(next)

print('Yes')  # 팬클럽 곰곰이를 무조건 만나게 된다.
