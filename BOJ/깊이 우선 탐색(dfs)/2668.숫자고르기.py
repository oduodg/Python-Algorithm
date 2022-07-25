import sys
input = sys.stdin.readline
n = int(input())
ans = []
line = [0] # 둘째줄
for _ in range(n):
    line.append(int(input()))

visited = [False for _ in range(n+1)]
stack1 = []
stack2 = []

def dfs(i):
    global stack1, stack2, ans
    stack1.append(i)
    cur = stack1[-1]
    next = line[cur]
    if not visited[next]: # 방문하지 않았다면
        stack1.append(next) # 스택에 push
        stack2.append(line[next])
        visited[next] = True # 방문 처리
        dfs(next)
    else: # 이미 방문한 스택이라면
        # stack1과 stack2의 집합을 비교한다.
        if set(stack1) == set(stack2): # 집합이 같으면
            ans += stack1 # 뽑힌 정수들을 추가
        else: # 집합이 다르면
            while stack1:
                # stack1의 정수들이 다른 집합에서는
                # 뽑힐 수도 있기 때문에
                # 방문 배열을 다시 초기화해주어야함
                visited[stack1.pop()] = False

        # 초기화
        stack1 = []
        stack2 = []


for i in range(1, n+1):
    dfs(i)

ans = sorted(set(ans))
print(len(ans))
for num in ans:
    print(num)
