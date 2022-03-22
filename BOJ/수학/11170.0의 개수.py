import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    n, m = map(int, input().split())
    ans = 0
    while n <= m:
        str_n = str(n)
        ans += str_n.count('0')
        n += 1
    print(ans)