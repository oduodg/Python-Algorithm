import sys
input = sys.stdin.readline
n = int(input())
l = []
total = 0 # 전체 사람의 수
for _ in range(n):
    x, a = map(int, input().split())
    l.append([x, a])
    total += a

l.sort(key=lambda x: (x[0], x[1])) # 마을 위치 순서로 정렬

# 우체국은 "마을"에 위치하는 것이 유리하다.
# 우체국이 위치한 마을의 사람들의 수는 고려하지 않아도 되므로
# (마을이 존재하지 않는)마을과 마을 사이에 위치하는 것은 불리함. 
# 우체국을 기준으로 마을 사람들의 수가 골고루 분포되어 있는 것이 좋음.
# 예를 들어 전체 사람이 10명이라면 5명과 5명 사이 중간에 우체국에 위치한 것이 유리하다.
# -> 전체 사람 수의 반이 되는 지점에 우체국을 세운다.

mid = 0
for i in range(n):
    mid += l[i][1]
    if mid >= total - mid:
        print(l[i][0])
        break
