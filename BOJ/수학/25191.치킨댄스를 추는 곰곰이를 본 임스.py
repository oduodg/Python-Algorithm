# 치킨 1마리 -> 콜라2개 + 맥주 1개
# 치킨 주문 수 <= 치킨집의 치킨 개수
n = int(input())  # 치킨집에 있는 치킨의 총 개수
a, b = map(int, input().split())  # 콜라의 개수 a, 맥주의 개수 b
drink = a//2 + b
if drink <= n:
    print(drink)
else:
    print(n)
