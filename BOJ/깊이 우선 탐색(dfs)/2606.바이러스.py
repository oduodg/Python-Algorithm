# 백준 2606번
import collections
import sys
input = sys.stdin.readline # 입력 가속

# 입력받기 -> n: 컴퓨터의 수, pair: 직접 연결된 컴퓨터 쌍의 수
n = int(input())
pair = int(input())

# 그래프 생성
graph = collections.defaultdict(list)
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1) # 방문한 노드를 담을 배열

def dfs(v): # v는 방문할 노드
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)
    return visited.count(True) - 1 # 1번 컴퓨터 수는 제외

print(dfs(1))