# 순서와 중복이 없다면 list보다 set을 사용하면 좋다. -> 시간초과 해결
# myCard를 list로 받으면 시간초과, set으로 받으면 통과

import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())
myCard = set(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

for card in cards:
    if card in myCard:
        print(1, end=' ')
    else:
        print(0, end=' ')
