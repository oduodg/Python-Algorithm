
from typing import List


class Solution:
    # 풀이 1. 오름차순 풀이
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    # 풀이 2. 짝수 번째 값 계산
    def arrayPairSum2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for n in nums[::2]:
            sum += n

        return sum

    # 풀이 3. 파이썬다운 방식
    def arrayPairSum3(self, nums: List[int]) -> int:
        return sum(sorted(nums[::2]))


# 결과 확인
nums = [1, 4, 3, 2, 5, 6]

slt = Solution()
print(slt.arrayPairSum(nums))
print(slt.arrayPairSum2(nums))
print(slt.arrayPairSum3(nums))
