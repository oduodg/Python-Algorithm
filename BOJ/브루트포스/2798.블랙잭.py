import sys, itertools
input = sys.stdin.readline # 입력 가속

n, m = map(int, input().split())
nums = list(map(int, input().split()))

it = list(itertools.combinations(nums, 3))
cards = [sum(card) for card in it if sum(card) <= m]
if m in cards:
    print(m)
else:
    cards.sort()
    print(cards[-1])

