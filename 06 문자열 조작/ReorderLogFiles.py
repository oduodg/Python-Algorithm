from typing import List

class Solution:
    # 풀이 1. 람다와 + 연산자를 이용
    def reorderLogFiles(selt, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits

# 결과 확인
logs = ["dig1 8 1 5 1", "leet1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

slt = Solution()
print(slt.reorderLogFiles(logs))