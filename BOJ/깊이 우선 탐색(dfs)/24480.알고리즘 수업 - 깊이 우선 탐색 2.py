import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)  # 방문 순서를 담을 배열
for _ in range(m):
    u, v = map(int, input().split())
    # 양방향 간선
    graph[u].append(v)
    graph[v].append(u)

stack = [r]  # 시작 노드를 스택에 담는다.
i = 1
while stack:
    curr = stack.pop()
    #print('curr:', curr)
    visited[curr] = True  # 방문
    if not ans[curr]:
        ans[curr] = i
        i += 1
    #print('ans:', ans[1:])
    for next in sorted(graph[curr]):  # 인접 노드 오름차순 정렬(pop은 뒤에서부터 되니까)
        if not visited[next]:  # 방문하지 않은 노드가 있다면
            stack.append(next)  # 스택에 추가

for order in ans[1:]:
    print(order)
