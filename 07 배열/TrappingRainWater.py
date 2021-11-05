from typing import List


class Solution:
    # 풀이 1. 투 포인터를 최대로 이동
    def trap(self, height: List[int]) -> int:
        # 예외처리
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(
                height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    # 풀이 2. 스택 쌓기
    def trap2(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우(현재 높이가 이전 높이보다 높을 때)
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):  # 스택이 비어있으면
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
            stack.append(i)
        return volume


# 결과 확인
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

slt = Solution()
print(slt.trap(height))
print(slt.trap2(height))
