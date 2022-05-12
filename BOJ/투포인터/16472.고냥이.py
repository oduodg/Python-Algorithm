import sys
input = sys.stdin.readline
n = int(input())  # 인식할 수 있는 알파벳 종류의 최대 개수
line = input().rstrip()

left, right = 0, 0
letter = set(line[left])  # 알파벳 종류를 담을 배열
ans = right - left + 1  # 문자열 최대 길이
cnt = 1  # 현재 문자열 길이

while right < len(line)-1:
    right += 1
    letter.add(line[right])

    if len(letter) > n:
        letter = set()
        left += 1
        right = left
        letter.add(line[left])

    cnt = right - left + 1
    ans = max(ans, cnt)
print(ans)
