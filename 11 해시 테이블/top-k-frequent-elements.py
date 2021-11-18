from typing import List
import collections
import heapq


class Solution:
    # 풀이 1. Counter를 이용한 음수 순 추출
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)  # {1: 3, 2: 2, 3: 1} 요소: 빈도 수
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))  # freqs[f]는 빈도 수, f는 요소
            # heapq = [(-3,1), (-2,2), (-1,3)] -> 가장 높은 빈도 수가 가장 작은 음수가 됨

        topk = list()
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출(가장 높은 빈도 수부터 추출)
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk

    # 풀이 2. 파이썬다운 방식
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


# 결과 확인
nums = [1, 1, 1, 2, 2, 3]
k = 3

slt = Solution()
print(slt.topKFrequent(nums, k))
print(slt.topKFrequent2(nums, k))
