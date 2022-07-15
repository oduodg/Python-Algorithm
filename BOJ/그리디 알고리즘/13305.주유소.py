import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# ans = 0

# for i in range(n-1, 0, -1): # 뒤에서부터 계산
#     min_price = min(price[:i])
#     ans += distance[i-1] * min_price

# print(ans)


ans = 0
min_price = price[0]
for i in range(n-1):
    min_price = min(price[i], min_price)
    ans += distance[i] * min_price

print(ans)