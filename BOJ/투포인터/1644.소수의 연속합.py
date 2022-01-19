import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 자연수 n

# 소수 판별 - 에라토스테네스의 체
num = [True] * (n+1)
num[0], num[1] = False, False
prime = []
for i in range(2, n+1):
    if num[i]: # True이면 소수
        prime.append(i)
        for j in range(i*2, n+1, i): # i의 배수는 모두 False 처리
            num[j] = False

# 연속된 소수의 합 - 투 포인터
start, end = 0, 0
total, cnt = 0, 0
while start < len(prime):
    if total < n:
        if end == len(prime): # end가 끝까지 간 경우, 반복문 탈출
            break
        total += prime[end]
        end += 1
    elif total > n:
        total -= prime[start]
        start += 1
    else: # total == n인 경우
        cnt += 1
        total -= prime[start]
        start += 1
print(cnt)