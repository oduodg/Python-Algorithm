# 백준 2667번
from sys import stdin

input = stdin.readline # 입출력 가속

# 입력받기 -> N: 지도(정사각형)의 크기
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)] # 그래프 생성, rstrip(): \n 제거

def dfs(i, j):
    global apt
    # 더 이상 집이 아닌 경우 종료
    if i < 0 or i >= N or \
        j < 0 or j >= N or \
            graph[i][j] != '1':
                return False

    # 집인 경우 실행
    apt += 1 # 집의 개수 카운트 1 증가
    graph[i][j] = '0' # 방문한 곳은 '0'으로 마킹
    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
    
    return apt

    
block = [] # 단지별 집의 개수를 요소로 갖는 리스트
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            apt = 0 # 집의 개수
            block.append(dfs(i,j))

print(len(block)) # 단지의 수
for apt in sorted(block):
    print(apt) # 집의 수

