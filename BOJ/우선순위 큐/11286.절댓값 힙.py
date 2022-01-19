import sys
import heapq

input = sys.stdin.readline # 입력 가속
n = int(input()) # 연산의 개수
heap = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, [abs(x), x])
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])