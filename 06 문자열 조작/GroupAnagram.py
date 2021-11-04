from typing import List
import collections


class Solution:
    # 풀이 1. 정렬하여 딕셔너리에 추가
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


# 결과 확인
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

slt = Solution()
print(slt.groupAnagrams(strs))
