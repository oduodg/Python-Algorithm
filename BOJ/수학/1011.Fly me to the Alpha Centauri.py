import sys
input = sys.stdin.readline # 입력 가속

def count_distance(d):
    n = 0
    while True:
        if d <= n * (n+1):
            break
        n += 1        
    if d <= n * n: # 이동거리 d가 제곱수보다 작거나 같으면
        return n +  (n -1)
    else: # 이동거리 d가 제곱수보다 크면
        return n + n

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x # 거리
    print(count_distance(d))