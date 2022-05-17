import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * n
for _ in range(m):
    u, v = map(int, input().split())
    # 양방향 간선
    graph[u].append(v)
    graph[v].append(u)

i = 0


def dfs(graph, r):
    global i
    visited[r] = True
    i += 1
    ans[r-1] = i
    for u in sorted(graph[r]):
        if not visited[u]:
            dfs(graph, u)

    return ans


for order in dfs(graph, r):
    print(order)
