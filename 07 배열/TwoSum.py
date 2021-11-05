from typing import List


class Solution:
    # 풀이 1. 브루트 포스로 계산
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 풀이 2. in을 이용한 탐색
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):  # i는 index, n은 value
            complement = target - n

            if complement in nums[i+1:]:  # nums[i]는 자기자신이므로 제외하고 다음 값부터 마지막 값까지 탐색
                # nums[i+1:]에서의 index 이므로 i+1 더해줌
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]

    # 풀이 3. 첫 번째 수를 뺀 결과 키 조회
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i  # nums_map = {2:0, 7:1, 11:2, 15:3}

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]

    # 풀이 4. 조회 구조 개선
    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i

    # 풀이 5. 투 포인터 이용
    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums) - 1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if sorted_nums[left] + sorted_nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            else:
                return sorted([nums.index(sorted_nums[left]), nums.index(sorted_nums[right])])


# 결과 확인
nums = [2, 7, 11, 15]
target = 9

slt = Solution()
print(slt.twoSum(nums, target))
print(slt.twoSum2(nums, target))
print(slt.twoSum3(nums, target))
print(slt.twoSum4(nums, target))
print(slt.twoSum5(nums, target))

print()
nums1 = [11, 7, 2, 15, ]
print(slt.twoSum(nums1, target))
print(slt.twoSum2(nums1, target))
print(slt.twoSum3(nums1, target))
print(slt.twoSum4(nums1, target))
print(slt.twoSum5(nums1, target))
