import sys
input = sys.stdin.readline

while True:
    sent = input().rstrip()
    if sent == '#':
        break
    else:
        sent = sent.lower()  # 소문자로 변경
        ans = sent.count('a') + sent.count('e') + \
            sent.count('i') + sent.count('o') + sent.count('u')
        print(ans)
