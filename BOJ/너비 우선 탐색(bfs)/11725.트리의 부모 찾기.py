from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
visited = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent = [0] * (n+1)  # 부모 노드를 담을 배열
q = deque([1])
visited[1] = True
while q:
    curr = q.popleft()
    for next in tree[curr]:
        if not visited[next]:
            q.append(next)
            visited[next] = True
            parent[next] = curr  # 부모 노드 저장

for p in parent[2:]:
    print(p)
