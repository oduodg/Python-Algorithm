import sys
input = sys.stdin.readline # 입력 가속

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

N = int(input()) # 수의 개수
nums = list(map(int, input().split()))
cnt = 0
for num in nums:
    if is_prime(num):
        cnt += 1
print(cnt)