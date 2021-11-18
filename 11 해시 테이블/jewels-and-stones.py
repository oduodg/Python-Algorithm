import collections


class Solution:
    # 풀이 1. 해시 테이블을 이용한 풀이
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}  # 해시 테이블(딕셔너리) 선언
        count = 0

        # 돌(S)의 빈도 수 계산s
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석(J)의 빈도 수 합산
        for char in J:
            if char in freqs:
                count += freqs[char]

        return count

    # 풀이 2. defaultdict를 이용한 비교 생략
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # 비교 없이 돌(S) 빈도 수 계산
        for char in S:
            freqs[char] += 1

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count

    # 풀이 3. Counter로 계산 생략
    def numJewelsInStones3(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
        count = 0
        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count

    # 풀이 4. 파이썬다운 방식
    def numJewelsInStones4(self, jewels: str, stones: str) -> int:
        return sum(s in J for s in S)


# 결과 확인
J = "aA"
S = "aAAbbbb"
slt = Solution()
print(slt.numJewelsInStones(J, S))
print(slt.numJewelsInStones2(J, S))
print(slt.numJewelsInStones3(J, S))
print(slt.numJewelsInStones4(J, S))
