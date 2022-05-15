import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    cnt = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        # 이동거리 = 속도 * (연료양/연료소비율) = v * (f/c)
        if v * (f/c) >= d:
            cnt += 1
    print(cnt)
