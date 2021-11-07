from typing import List


class Solution:
    # 풀이 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out. append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out

    # 풀이 2. for문 3개 -> 시간복잡도 O(n) * 3 = O(n)
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        front, back = [0 for i in range(len(nums))], [0 for i in range(
            len(nums))]  # front는 앞에서부터 곱한 요소들을 저장, back은 뒤에서부터 곱한 요소들을 저장
        result = []
        '''
        nums = [a,b,c,d]
        front = [1, a, a*b, a*b*c]
        back = [b*c*d, c*d, d, 1]
        '''
        p = 1
        for i in range(len(nums)):
            front[i] = p
            p = p * nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):  # i는 맨 뒤의 바로 앞에서부터 맨 앞까지
            back[i] = p
            p = p * nums[i]

        for i in range(len(nums)):
            result.append(front[i]*back[i])

        return result


# 결과 확인
nums = [1, 2, 3, 4]

slt = Solution()
print(slt.productExceptSelf(nums))
print(slt.productExceptSelf2(nums))
