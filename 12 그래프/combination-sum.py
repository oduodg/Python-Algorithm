from typing import List


class Solution:
    # 풀이 1. DFS로 중복 조합 그래프 탐색
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


# 결과 확인
candidates = [2, 3, 6, 7]
target = 7

candidates2 = [2, 3, 5]
target2 = 8

slt = Solution()
print(slt.combinationSum(candidates, target))
print(slt.combinationSum(candidates2, target2))
