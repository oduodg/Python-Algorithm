import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
for _ in range(n):
    word = input().rstrip()
    dic[word] = 0

cnt = 0
for _ in range(m):
    word = input().rstrip()
    if word in dic:
        cnt += 1
print(cnt)
