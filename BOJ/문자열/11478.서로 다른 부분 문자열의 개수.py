import sys
input = sys.stdin.readline

word = input().rstrip()
sub = []
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        sub.append(word[i:j])

print(len(set(sub)))
