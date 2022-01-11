import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())

for i in itertools.combinations_with_replacement(range(1, N+1), M): # 중복 조합
    print(*i)