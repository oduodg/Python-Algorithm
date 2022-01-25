import sys
input = sys.stdin.readline # 입력 가속

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif d == 0 or r1 + r2 < d or max(r1-r2, r2-r1) > d:
        print(0)
    elif r1 + r2 == d or max(r1-r2, r2-r1) == d:
        print(1)
    elif max(r1-r2, r2-r1) < d and r1 + r2 > d:
        print(2)