import sys
input = sys.stdin.readline # 입력 가속

def is_prime(n):
    num = [False, False] + [True] * (n-1) # 0 ~ n까지
    for i in range(2, n+1):
        if num[i]:
            for j in range(i*2, n, i):
                num[j] = False
    return [i for i in range(2, n) if num[i] == True]

num = is_prime(10000) # 10000까지의 모든 소수(입력 n은 10000보다 작거나 같은 모든 짝수임)

t = int(input()) # 테스트 케이스의 개수
for _ in range(t):
    n = int(input())
    # n은 짝수이므로 left + right = n 임.
    left, right = n//2, n//2 # 두 소수의 차이가 가장 작은 것부터 찾아야하므로 중간부터 찾기
    while True:
        if left in num and right in num:
            print(left, right)
            break
        else:
            left -= 1 # 왼쪽은 하나씩 감소시키고
            right += 1 # 오른쪽은 하나씩 증가시킴