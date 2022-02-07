n = int(input())
p = list(map(int, input().split()))
answer = [0] * n
for i in range(n):
    if p[i] == 0:  # 왼쪽에 나보다 큰 사람이 0명인 경우
        for j in range(n):
            if answer[j] == 0:
                answer[j] = i+1
                break
    else:
        zero_cnt = 0
        for j in range(n):
            if answer[j] == 0:
                zero_cnt += 1
                if zero_cnt == p[i]+1:
                    answer[j] = i+1
                    break

for num in answer:
    print(num, end=' ')
