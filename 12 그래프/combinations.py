from typing import List
import itertools


class Solution:
    # 풀이 1. DFS로 k개 조합 생성
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

    # 풀이 2. itertools 모듈 사용
    def combine2(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, itertools.combinations(range(1, n+1), k)))


# 결과 확인
n = 4
k = 2
slt = Solution()
print(slt.combine(4, 2))
print(slt.combine2(4, 2))
