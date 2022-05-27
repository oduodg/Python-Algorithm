import sys
import heapq
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x[0], x[1]))  # 시작 시간이 빠른 순 -> 종료 시간이 빠른 순으로 정렬
heap = []
heapq.heappush(heap, a[0][1])  # 첫 번째 강의의 끝나는 시간을 넣어줌
for i in range(1, n):
    # 같은 강의실을 사용할 수 있는 경우
    if heap[0] <= a[i][0]:  # 이전 강의의 종료 시간이 다음 강의의 시작 시간보다 빠르거나 같을 때
        heapq.heappop(heap)  # 이전 강의의 종료 시간을 pop하고
        heapq.heappush(heap, a[i][1])  # 다음 강의 종료 시간을 push해서 갱신
    # 새로운 강의실을 개설해야 할 경우
    else:
        heapq.heappush(heap, a[i][1])  # 새로운 강의실에서 시작되는 강의의 종료 시간을 push

print(len(heap))  # heap의 길이가 강의실의 개수가 된다.
