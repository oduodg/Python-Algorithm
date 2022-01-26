import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 선수의 수
picked = {}
for _ in range(n):
    last_name = input()
    if last_name[0] in picked:
        picked[last_name[0]] += 1
    else:
        picked[last_name[0]] = 1

answer = []
for key,value in picked.items():
    if value >= 5:
        answer.append(key)

if answer:
    print(''.join(sorted(answer)))
else:
    print("PREDAJA")