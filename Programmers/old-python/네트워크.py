# 백준 바이러스 문제와 유사함
import collections

def solution(n, computers): # DFS 풀이
    # 그래프 생성
    graph = collections.defaultdict(list)
    for key in range(n):
        graph[key] # 아무것도 연결되어 있지 않은 컴퓨터가 있을 수 있으므로

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)

    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                dfs(w)

    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i) # dfs로 노드의 끝까지 돌 수 있는 만큼 다 돌면
            answer += 1 # 네트워크 1개를 찾은 것이므로 +1

    return answer

def solution2(n, computers): # BFS 풀이
    visited = [False] * n

    def bfs(v):
        visited[v] = True # 노드 v 방문 처리
        q = collections.deque([v]) # 노드v를 큐에 삽입

        while q:
            v = q.popleft() # 노드v를 큐에서 꺼낸다.
            
            for i in range(n):
                if computers[v][i] == 1 and not visited[i]: # 연결되어 있고 방문하지 않았다면
                    q.append(i) # 큐에 삽입
                    visited[i] = True # 방문처리

    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer

# Test Case
TC1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n1 = 3

TC2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n2 = 3

print(solution(n1, TC1))
print(solution(n2, TC2))

print(solution2(n1, TC1))
print(solution2(n2, TC2))