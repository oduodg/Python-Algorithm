from typing import List
import heapq
class Solution:
    def reconsturctQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 우선순위 큐 이용
        # 첫 번째 값 -> 최대 힙, 두번째 값 -> 삽입 인덱스
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

# 결과 확인
slt = Solution()
test_case1 = [[7,0], [4,4], [7,1], [5,0],[6,1],[5,2]]
print(slt.reconsturctQueue(test_case1))