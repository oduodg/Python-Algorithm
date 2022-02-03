n = int(input())
def is_prime(n):
    num = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if num[i]:
            for j in range(i*2, n+1, i): # 에라토스테네스의 체
                num[j] = False
    return [i for i in range(2, n+1) if num[i] == True]

num = is_prime(n)
i = 0
while True:
    if n == 1:
        break
    if n % num[i] == 0:
        print(num[i])
        n = n // num[i]
        i = 0
    else:
        i += 1

# 더 간단한 코드
"""
n = int(input())
m = 2
while n != 1:
    if n %m == 0:
        print(m)
        n = n//m
    else:
        m += 1 
"""