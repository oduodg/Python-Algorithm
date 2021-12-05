## 깊이 우선 탐색(DFS; Depth First Search)

: 특정 노드에서 시작해 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법(자식들을 우선으로 탐색)

> 특징
> 
- 전체적으로 위에서 아래로 `깊게` 탐색이 진행된다.
- 모든 노드를 방문하고자 하는 경우에 이 방법을 선택한다.
- 자기 자신을 호출하는 `순환 알고리즘`의 형태를 가지고 있다.
- 전위 순회(Pre-Order Traversals)를 포함한 다른 형태의 트리 순회는 모두 DFS의 한 종류이다.
- 어떤 노드를 방문했었는지 여부를 반드시 검사해야한다.(검사하지 않을 경우 무한루프에 빠질 위험이 있다.)

> 구현 방법
> 
1.  `재귀` 구조
2.  `스택`
    - 방문한 노드들을 스택에 넣어놨다가 꺼내서 작업한다.

> 시간 복잡도
> 

그래프(정점의 수: N, 간선의 수: E)의 모든 간선을 조회한다.

- 인접 리스트로 표현된 그래프: O(N+E)
- 인접 행렬로 표현된 그래프: O(N^2)

> Code
> 

```python
visited = [False] * (N+1) # 1번 노드부터 시작이므로 인덱스를 1~N으로 맞추기 위해 크기가 N+1인 배열 생성

def dfs(v): # v는 탐색할 노드
	#print(v, end=' ')
	visited[v] = True # 노드v 방문 처리 
	for w in graph[v]: # 노드v와 인접한 노드 중에서
			if not visited[w]: # 방문하지 않은 노드라면
					dfs(w) # 재귀 호출
```

```python
def dfs(v, visited=[]): # v는 탐색할 노드
	#print(v, end=' ')
	visited.append(v) # 노드v 방문 처리
	for w in graph[v]: # 노드v와 인접한 노드 중에서
			if w not in visited: # 방문하지 않은 노드라면
					visited = dfs(w, visited)
	return visited
```

## 너비 우선 탐색(BFS; Breath First Search)

: 시작 노드를 방문한 후 시작 노드에 있는 인접한 모든 노드들을 우선 방문(형제들을 우선으로 탐색)

> 특징
> 
- 깊게 탐색하기 전에 양옆으로 `넓게` 탐색이 진행된다.
- 재귀 구현이 불가능하다.
- 어떤 노드를 방문했었는지 여부를 반드시 검사해야한다.(검사하지 않을 경우 무한루프에 빠질 위험이 있다.)

> 구현 방법
> 
1. `큐`를 이용한 반복 구조

> 시간 복잡도(DFS와 동일)
> 

그래프(정점의 수: N, 간선의 수: E)의 모든 간선을 조회한다.

- 인접 리스트로 표현된 그래프: O(N+E)
- 인접 행렬로 표현된 그래프: O(N^2)

> Code
> 

```python
import collections

def bfs(v):
    visited[v] = True # 노드v 방문 처리
    queue = collections.deque([v]) # 노드v 큐에 삽입
    while queue:
        v = queue.popleft() # 노드v를 큐에서 꺼낸다.
        #print(v, end= ' ')
        for w in graph[v]: # 노드v와 인접한 노드 중에서
            if not visited[w]: # 방문하지 않은 노드가 있다면
                queue.append(w) # 큐에 삽입
                visited[w] = True # 방문 처리
```

```python
def bfs(v):
    visited = [v] # 노드v 방문 처리
    queue = collections.deque([v]) # 노드v 큐에 삽입
    while queue:
        v = queue.popleft() #노드v를 큐에서 꺼낸다.
				#print(v, end=' ')
        for w in graph[v]: # 노드v와 인접한 노드 중에서
            if w not in visited: # 방문하지 않은 노드가 있다면
                visited.append(w) # 방문 처리
                queue.append(v) # 큐에 삽입
    return visited
```