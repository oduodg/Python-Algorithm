import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

house = [] # 집 위치
chicken = [] # 치킨집 위치
for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            house.append((r+1,c+1))
        elif city[r][c] == 2:
            chicken.append((r+1,c+1))

distance = [[0 for _ in range(len(house))] for _ in range(len(chicken))] # 치킨집을 기준으로 각 집과의 치킨 거리
for i in range(len(chicken)):
    r1 = chicken[i][0]
    c1 = chicken[i][1]
    for j in range(len(house)):
        r2 = house[j][0]
        c2 = house[j][1]
        distance[i][j] = abs(r1-r2) + abs(c1-c2)

cases = list(combinations(distance, m))
ans = []

for case in cases:
    case_distance = 0
    for i in range(len(house)):
        chicken_distance = sys.maxsize
        for j in range(m):
            chicken_distance = min(case[j][i], chicken_distance)
        case_distance += chicken_distance
    ans.append(case_distance)

print(min(ans))