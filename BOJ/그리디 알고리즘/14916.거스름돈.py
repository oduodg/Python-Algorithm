import sys
input = sys.stdin.readline
n = int(input())  # 거스름돈 액수

if n == 1 or n == 3:
    print(-1)
    sys.exit()

if n % 5 == 0:
    ans = n//5
elif n % 5 == 1:  # 5원 1개를 빼서 나머지를 6원으로 만듬
    ans = (n//5 - 1) + 3  # 6원을 2원짜리 3개로
elif n % 5 == 2:
    ans = n//5 + 1  # 나머지 2원을 2원짜리 1개로
elif n % 5 == 3:  # 5원 1개를 빼서 나머지를 8원으로 만듬
    ans = ((n//5 - 1) + 4)  # 8원을 2원짜리 4개로
else:
    ans = n//5 + 2

print(ans)
