import sys
input = sys.stdin.readline
total = [0,0,0,0,0]
for i in range(5):
    score = input().split()
    score = sum(list(map(int, score)))
    total[i] = score

winner = max(total)
print(total.index(winner)+1, winner)