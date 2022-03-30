import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()

alphabet1 = [0] * 26
alphabet2 = [0] * 26


def solution(word1, word2):
    result = 0
    for alpha in word1:
        alphabet1[ord(alpha)-97] += 1  # 영문 소문자 아스키코드: 97 ~ 122
    for alpha in word2:
        alphabet2[ord(alpha)-97] += 1

    for i in range(26):
        result += abs(alphabet1[i] - alphabet2[i])
    return result


print(solution(word1, word2))
