import sys
input = sys.stdin.readline # 입력 가속

N = int(input()) # 단어의 개수

words = []
for _ in range(N):
    word = input()
    words.append(word)

for word in sorted(sorted(set(words)), key=len):
    print(word, end='')
