from collections import deque

n = int(input())
cards = [i for i in range(1, n+1)]
cards = deque(cards)
discard = []

while len(cards) != 1:
    discard.append(cards.popleft())
    cards.append(cards.popleft())

for card in discard:
    print(card, end=' ')

print(cards[0])
