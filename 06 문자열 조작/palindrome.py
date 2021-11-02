from typing import Deque
import collections
import re

class Solution:
    # 풀이 1. 리스트로 변환
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 문자가 영문자나 숫자이면
                strs.append(char.lower()) # 소문자로 변환해서 strs에 추가

        while len(strs) > 1:
            if strs.pop() != strs.pop(0): # 맨 앞 요소와 맨 뒤 요소가 같지 않으면 //pop(0) -> O(n)
                return False

        return True

    # 풀이 2. 데크 자료형을 이용한 최적화
    def isPalindrome2(self, s: str) -> bool:
        strs: Deque = collections.deque() # 자료형을 데크로 선언
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop() != strs.popleft(): # 데크의 popleft() -> O(1)
                return False

        return True

    # 풀이 3. 슬라이싱 사용
    def isPalindrome3(self, s: str) -> bool:
        s = s.lower() # 입력받은 문자열을 모두 소문자로 변환
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1] # 슬라이싱 -> 원본 문자열이 뒤집은 문자열과 같은지 확인


# 결과 확인
s = "A man, a plan, a canal: Panama"
slt = Solution()
print(slt.isPalindrome(s))
print(slt.isPalindrome2(s))
print(slt.isPalindrome3(s))

s = "race a car"
print(slt.isPalindrome(s))
print(slt.isPalindrome2(s))
print(slt.isPalindrome3(s))