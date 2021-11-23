from typing import List
import itertools


class Solution:
    # 풀이 1. DFS를 활용한 순열 생성
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results
    # 풀이 2. itertools 모듈 사용

    def permute2(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))


nums = [1, 2, 3]
slt = Solution()
print(slt.permute(nums))
print(slt.permute2(nums))
