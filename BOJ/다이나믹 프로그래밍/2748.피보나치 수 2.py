fibo_dp = [0] * 91

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif fibo_dp[n] != 0:
        return fibo_dp[n]
    else:
        fibo_dp[n] = fibo(n-1) + fibo(n-2)
    return fibo_dp[n]

n = int(input())
print(fibo(n))