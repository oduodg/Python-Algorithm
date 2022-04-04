import sys, copy
input = sys.stdin.readline

n = int(input())  # 단어의 개수 n
words = []
for _ in range(n):
    word = input().rsplit()
    words.append(*word)

words.sort(key=len)
ans = copy.deepcopy(words) # 원본 배열 보존을 위해 깊은 복사

for i in range(len(words)-1):
    for j in range(i+1, len(words)):
        if words[j].startswith(words[i]):
            ans.remove(words[i])
            break

print(len(ans))
