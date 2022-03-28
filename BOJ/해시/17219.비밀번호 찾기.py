import sys
input = sys.stdin.readline
n, m = map(int, input().split())

account = {}
for _ in range(n):
    url, pwd = input().split()
    account[url] = pwd

for _ in range(m):
    target = input().rstrip()
    print(account[target])