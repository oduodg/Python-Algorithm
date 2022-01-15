import sys, heapq
input = sys.stdin.readline # 입력 가속

n = int(input()) # 연산의 개수
heap = []

def minHeap(x):
    if x == 0:
        if heap: 
            print(heapq.heappop(heap))
        else:
            print(0)
    elif type(x) == int and x > 0:
        heapq.heappush(heap, x)

for _ in range(n):
    minHeap(int(input()))