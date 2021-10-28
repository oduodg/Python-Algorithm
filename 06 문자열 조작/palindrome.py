# 풀이1. 리스트로 변환
from typing import Collection


def isPalindrome(s: str) -> bool:
    strs = [] # 빈 리스트 생성: 영문자와 숫자만을 담는다.
    for char in s:
        if char.isalnum(): # 문자가 영문자, 숫자이면
            strs.append(char.lower()) # 소문자로 변환하고 리스트에 추가한다.
    
    #팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): # 맨 앞의 요소와 맨 뒤의 요소가 다른지 비교한다.
            return False
    return True


#s = input()
#print(isPalindrome(s))

# 풀이2. 데크 자료형을 이용한 최적화
import collections
from typing import Deque

def isPalindrome2(s: str) -> bool:
    # 자료형을 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # deque의 popleft()는 왼쪽에서 pop을 가능하게 한다.
            return False
    return True

#s2 = input()
#print(isPalindrome2(s2))

# 풀이3. 슬라이싱 사용
import re

def isPalindrome3(s: str) -> bool:
    s = s.lower() # 소문자로 변환
    s = re.sub('[^a-z0-9]','',s)
    
    return s == s[::-1] #슬라이싱, 문자열 뒤집은 것이 원본과 같은지 확인


s3 = input()
print(isPalindrome3(s3))