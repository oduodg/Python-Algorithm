import sys
input = sys.stdin.readline # 입력 가속

# 파이썬에서는 재귀를 무한정 허용할 경우 생길 수 있는 문제들이 있다.
# 이 문제의 경우 노드의 개수(배추의 개수)가 최대 2500개까지 있을 수 있으므로
# 런타임 에러(RecursionError)가 발생할 수 있다.
# 아래 코드를 추가하여 재귀 호출의 제한을 충분히 늘려주면 런타임 에러 발생을 방지할 수 있다.
sys.setrecursionlimit(3000)

# 입력받기 -> t: 테스트 케이스 개수, m: 배추밭 가로길이, n: 배추밭 세로길이, k: 배추의 개수
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    # 그래프 생성(인접 행렬)
    adj = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        adj[b][a] = 1 # a가 x축, b가 y축이므로 배열에서는 adj[b][a]

    def dfs(i, j):
        # 배추가 아닌 경우 종료
        if i < 0 or i >= n or \
            j < 0 or j >= m or \
                adj[i][j] != 1:
            return

        adj[i][j] = 0 # 이미 탐색한 곳은 0으로 체크

        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1 ,j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for b in range(n):
        for a in range(m):
            if adj[b][a] == 1:
                dfs(b, a) # 탐색 시작
                # 탐색 후 카운트 1 증가
                count += 1

    print(count)