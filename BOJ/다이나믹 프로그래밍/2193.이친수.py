n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp = [0, 1, 1] + [0] * (n-2)
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])