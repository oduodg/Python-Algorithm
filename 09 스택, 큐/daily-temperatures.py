from typing import List


class Solution:
    # 풀이 1. 스택 값 비교
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 디플트는 0 -> 만약 더 높은 온도가 나오지 않아 스택이 비워지지 않았다면 해당 인덱스는 없음
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


# 결과 확인
T = [73, 74, 75, 71, 69, 72, 76, 73]

slt = Solution()
print(slt.dailyTemperatures(T))
