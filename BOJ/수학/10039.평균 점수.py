import sys
input = sys.stdin.readline # 입력 가속

total = 0
for _ in range(5):
    score = int(input())
    if score >= 40:
        total += score
    else:
        total += 40

print(total//5)