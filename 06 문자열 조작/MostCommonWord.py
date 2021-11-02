from typing import List
import re
import collections

class Solution:
    # 풀이 1. 리스트 컴프리헨션, Counter 객체 사용
    def mostCommonword(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)
        
        return counts.most_common(1)[0][0]

# 결과 확인
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

slt = Solution()
print(slt.mostCommonword(paragraph, banned))