import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 로프의 개수
ropes = []
for _ in range(n):
    ropes.append(int(input())) # 각 로프의 최대 중량
ropes.sort(reverse=True) # 내림차순으로 정렬
w = [ropes[i]*(i+1) for i in range(n)]
print(max(w))