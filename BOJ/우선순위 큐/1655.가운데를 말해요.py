import sys
import heapq
input = sys.stdin.readline  # 입력 가속

left = []  # Max Heap => left[0]이 max값
right = []  # min Heap => right[0]이 min값

n = int(input())  # 정수의 개수 n

for _ in range(n):
    if len(left) == len(right):
        heapq.heappush(left, int(input()) * (-1))
    else:
        heapq.heappush(right, int(input()))
    if left and right and left[0] * (-1) > right[0]:
        big = heapq.heappop(left) * (-1)
        small = heapq.heappop(right) * (-1)
        heapq.heappush(left, small)
        heapq.heappush(right, big)

    print(left[0] * (-1))
