# 220705 풀이
def solution(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Test Case
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution(nums1, target1))

nums2 = [3, 2, 4]
target2 = 6
print(solution(nums2, target2))

nums3 = [3, 3]
target3 = 6
print(solution(nums3, target3))
