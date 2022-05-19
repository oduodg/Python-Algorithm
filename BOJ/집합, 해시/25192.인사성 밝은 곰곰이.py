# 처음 채팅만 -> 곰곰티콘
import sys
input = sys.stdin.readline
n = int(input())
chat = []
gomgom = {}
for _ in range(n):
    id = input().rstrip()
    chat.append(id)

cnt = 0
for id in chat:
    if id == 'ENTER':  # 새로운 사람 입장
        gomgom = {}  # 초기화
    else:
        if id not in gomgom:
            gomgom[id] = True
            cnt += 1

print(cnt)
