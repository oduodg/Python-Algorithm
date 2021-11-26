from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)  # 거리를 나타내는 변수 dist

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)  # time = 0, node = k
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1


# 결과 확인
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

times2 = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [
    4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]
n2 = 8
k2 = 3

slt = Solution()
print(slt.networkDelayTime(times, n, k))
print(slt.networkDelayTime(times2, n2, k2))
