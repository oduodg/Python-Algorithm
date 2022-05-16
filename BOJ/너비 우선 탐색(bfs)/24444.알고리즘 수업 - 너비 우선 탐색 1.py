from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 인접 정점 집합
visited = [False] * (n+1)  # 방문 표시 배열
ans = [0] * n  # 정점의 방문 순서를 담을 배열
q = deque([])
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q.append(r)  # 시작 정점 큐에 추가
visited[r] = True  # 방문
i = 0  # 순서
while q:
    curr = q.popleft()
    i += 1  # 순서 증가
    ans[curr-1] = i  # 정점의 방문 순서 담기
    if graph[curr]:  # 인접 정점이 있으면
        for u in sorted(graph[curr]):  # 인접 정점 중에
            if not visited[u]:  # 방문하지 않은 정점을
                q.append(u)  # 큐에 추가
                visited[u] = True  # 방문

for order in ans:
    print(order)
