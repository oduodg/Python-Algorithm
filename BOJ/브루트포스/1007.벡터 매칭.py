import sys, math
from itertools import combinations
input = sys.stdin.readline
t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    n = int(input()) # 점의 개수
    p = []
    total_x = 0
    total_y = 0
    for _ in range(n):
        x, y = map(int, input().split()) # 점의 좌표
        p.append((x,y))
        total_x += x
        total_y += y
    
    # n//2(절반)개의 점 선택해서 빼주기
    subtract = list(combinations(p, n//2))
    ans = sys.maxsize
    for dots in subtract[:len(subtract)//2]: # 조합의 절반까지만 범위를 줄이는 것이 핵심
        subtract_x = 0
        subtract_y = 0
        for dot in dots:
            subtract_x += dot[0] *2 # total_x에서 dot[0]은 한번 더해진 상태이므로 2번 빼야 결과적으로 1번 빼준 상태가 된다.
            subtract_y += dot[1] *2 # total_y에서 dot[1]은 한번 더해진 상태이므로 2번 빼야 결과적으로 1번 빼준 상태가 된다.
        ans = min(math.sqrt((total_x - subtract_x)**2 + (total_y - subtract_y)**2), ans)
    
    print(ans)