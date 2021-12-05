# 백준 1260번
from sys import stdin
import collections

input = stdin.readline

# 입력받기 -> N:정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)] # 정점 N개에 대한 그래프 생성
visited = [False] * (N+1) # 방문한 노드를 담을 배열(인덱스를 맞추기 위해 (N+1)크기의 배열 생성)

# 간선 연결
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 그래프이므로 양쪽으로 연결

# 그래프 정렬(문제조건: 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문)
for v in range(1, N+1):
    graph[v].sort()

# Depth First Search
def dfs(v): # v는 탐색할 노드
    print(v, end=' ')
    visited[v] = True # 노드v 방문 처리
    for w in graph[v]: # 노드v와 인접한 노드 중에서
        if not visited[w]: # 방문하지 않은 노드가 있다면
            dfs(w) # 재귀 호출

# Breadth First Search
def bfs(v):
    visited[v] = True # 노드v 방문 처리
    queue = collections.deque([v]) # 노드v 큐에 삽입
    while queue:
        v = queue.popleft() # 노드v를 큐에서 꺼낸다
        print(v, end= ' ')
        for w in graph[v]: # 노드v와 인접한 노드 중에서
            if not visited[w]: # 방문하지 않은 노드가 있다면
                queue.append(w) # 큐에 삽입
                visited[w] = True # 방문 처리

# 함수 호출
dfs(V)
# 방문 노드 초기화
visited = [False] * (N+1)
print()
bfs(V)