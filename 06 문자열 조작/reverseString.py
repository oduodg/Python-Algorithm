from typing import List

class Solution:
    # 풀이 1. 투 포인터를 이용한 스왑
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) -1
        s[left], s[right] = s[right], s[left]

        while left < right:
            left += 1
            right -= 1
        
        print(s) # 결과 확인하기 위한 출력, 답안에서는 제거할 것

    # 풀이 2. 파이썬다운 방식
    def reverseString2(self, s: List[str]) -> None:
        s.reverse()

        print(s) # 결과 확인하기 위한 출력, 답안에서는 제거할 것

# 결과 확인
s = ["h","e","l","l","o"]
s1 = ["h","e","l","l","o"]
slt = Solution()
slt.reverseString(s)
slt.reverseString2(s1)

s2 = ["H","a","n","n","a","h"]
s3 = ["H","a","n","n","a","h"]
slt.reverseString(s2)
slt.reverseString2(s3)
