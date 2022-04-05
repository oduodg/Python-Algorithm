import copy
n = int(input())
m = copy.deepcopy(n)
cnt = [0 for _ in range(10)] # 0~9까지 카운트할 배열
digit = 1 # 자릿수 확인하는 변수

while n != 0:
    a, b = divmod(n, 10)

    # 0 ~ 9 카운트    
    for i in range(10):
        cnt[i] += (a+1) * digit

    # 0은 맨 앞자리에 올 수 없으므로 카운트에서 빼준다
    cnt[0] -= digit

    # 9로 맞춰준 뒤의 차이값을 카운트에서 빼주기
    for i in range(b+1, 10):
        cnt[i] -= digit

    # 1의 자리 수가 아닌 경우 차이값 빼주기
    if digit != 1:
        cnt[b] -= (n+1)*digit - m - 1

    digit *= 10
    n = n//10

# 답 출력
for i in cnt:
    print(i, end=' ')