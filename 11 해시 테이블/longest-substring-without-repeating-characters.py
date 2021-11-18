class Solution:
    # 풀이 1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0  # start는 첫 번째 포인터
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length


# 결과 확인
s = "abcabcbb"
s1 = "bbbbb"
s2 = "pwwkew"
s3 = "tmmzuxt"

slt = Solution()
print(slt.lengthOfLongestSubstring(s))
print(slt.lengthOfLongestSubstring(s1))
print(slt.lengthOfLongestSubstring(s2))
print(slt.lengthOfLongestSubstring(s3))
