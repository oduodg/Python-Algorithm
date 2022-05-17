from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())  # n: 정점의 수, m: 간선의 수, r: 시작 노드
visited = [False] * (n+1)  # 방문 표시 배열
graph = [[] for _ in range(n+1)]  # 간선 정보를 담을 그래프
ans = [0] * n  # 방문 순서를 담을 배열
for _ in range(m):
    u, v = map(int, input().split())
    # 양방향 간선
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])  # 시작 노드를 담아준다.
visited[r] = True  # 방문 표시
i = 0  # 방문 순서
while q:
    curr = q.popleft()  # 노드를 꺼내고
    i += 1  # 방문 순서를 증가시키고
    ans[curr-1] = i  # 방문 순서 담기

    for u in sorted(graph[curr], reverse=True):  # 인접한 정점들 중 (내림차순으로)
        if not visited[u]:  # 방문하지 않은 정점들을
            q.append(u)  # 추가하고
            visited[u] = True  # 방문 표시

for order in ans:
    print(order)
