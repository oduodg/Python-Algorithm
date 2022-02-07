import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())  # 보석 n개, 가방 k개
gem = []  # 보석 힙
for _ in range(n):
    m, v = map(int, input().split())  # 보석의 무게 m, 가격 v
    heapq.heappush(gem, [m, v])

w = []  # 무게 힙
for i in range(k):
    c = int(input())  # 가방에 담을 수 있는 최대 무게 c
    heapq.heappush(w, c)

max_v = 0  # 최대 가격
capable = []  # bag에 담을 수 있는(bag보다 무게가 적은) 보석 힙
while w:
    bag = heapq.heappop(w)
    while gem and bag >= gem[0][0]:  # bag보다 무게가 적은 보석들은
        [weight, price] = heapq.heappop(gem)  # gem에서 pop하고
        heapq.heappush(capable, -price)  # capable에 -price로 push(최소힙이므로 -)

    if capable:  # 담을 수 있는 보석이 있으면
        max_v -= heapq.heappop(capable)  # 가격이 가장 높은 보석을 pop해서 가격 더하기

print(max_v)