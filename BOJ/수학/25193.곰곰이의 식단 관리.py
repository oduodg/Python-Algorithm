import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
chicken = s.count('C')
other = n - chicken

ans = 0

if other == 0:
    ans = n

start = 0
while other:
    end = start + (chicken // (other+1))
    chicken -= end
    other -= 1
    ans = max(ans, end-start)

ans = max(ans, chicken)

print(ans)
