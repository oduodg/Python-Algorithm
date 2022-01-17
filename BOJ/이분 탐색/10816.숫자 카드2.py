import sys, collections
input = sys.stdin.readline # 입력 가속

n = int(input())
cards = collections.Counter(map(int, input().split()))
m = int(input())
targets = map(int, input().split())

for target in targets:
    if target in cards:
        print(cards[target], end=" ")
    else:
        print(0, end=" ")