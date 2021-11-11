class Solution:
    # 풀이 1. 스택 일치 여부 판별
    def isValid(self, s: str) -> bool:
        stack = []
        table = {  # key: value
            ')': '(',
            '}': '{',
            ']': '[',
        }

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:  # table의 key에 해당하지 않으면 (value로 착각하지 말 것!)
                stack.append(char)
            elif not stack or table[char] != stack.pop():  # 딕셔너리[key] = value
                return False

        return len(stack) == 0  # 전부 짝 맞춰 pop 됐으면 스택이 비어있으므로 길이가 0이고 True 리턴


# 결과 확인
s = '()[]{}'

slt = Solution()
print(slt.isValid(s))
