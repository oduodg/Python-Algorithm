T = int(input())

answer = []
for _ in range(T):
    num = int(input())
    answer.append(num)

for i in range(len(answer)):
    print(sorted(answer)[i])