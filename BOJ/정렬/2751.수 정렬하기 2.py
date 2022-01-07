import sys
input = sys.stdin.readline
T = int(input())
answer =[]
for _ in range(T):
    num = int(input())
    answer.append(num)

for num in sorted(answer):
    print(num)