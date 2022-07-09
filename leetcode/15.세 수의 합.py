from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        ans = []
        nums.sort()  # 오름차순 정렬

        for i in range(len(nums) - 2):
            # 중복된 값 스킵
            if i > 0 and nums[i] == nums[i-1]:  # 첫번째 인덱스 0은 스킵하면 안되므로 i > 0
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                tmp = nums[left] + nums[i] + nums[right]
                if tmp == 0:
                    ans.append([nums[left], nums[i], nums[right]])
                    # 중복되는 숫자는 스킵하기
                    # 왼쪽 중복 숫자 스킵:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 오른쪽 중복 숫자 스킵
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # 스킵 처리 후
                    left += 1
                    right -= 1
                elif tmp < 0:
                    left += 1
                else:
                    right -= 1

        return ans


# Test Case
nums1 = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums1))  # [[-1, 0, 1], [-1, 2, -1]]

nums2 = []
print(Solution().threeSum(nums2))  # []

nums3 = [0]
print(Solution().threeSum(nums3))  # []
