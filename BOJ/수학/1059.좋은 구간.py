import sys
input = sys.stdin.readline
l = int(input())  # 집합 s의 크기
s = [0] + sorted(list(map(int, input().split())))  # 집합 s
n = int(input())

a = 0
b = 0

if n in s:
    print(0)
else:
    for num in s:
        if num < n:
            a = num + 1
        else:
            b = num - 1
            break
    print((n-a)*(b-n) + (b-a))