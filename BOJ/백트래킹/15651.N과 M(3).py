import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())

for i in itertools.product(range(1, N+1), repeat = M):
    print(*i)
