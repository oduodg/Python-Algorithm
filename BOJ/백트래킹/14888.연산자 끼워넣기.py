import sys
input = sys.stdin.readline
n = int(input())  # n개의 수
num = list(map(int, input().split()))  # 수
plus, minus, multi, div = map(int, input().split())
max_val = -1e9  # -10억
min_val = 1e9  # 10억


def dfs(curr, total):
    global plus, minus, multi, div, max_val, min_val

    if curr == n:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return

    if plus:
        plus -= 1
        dfs(curr+1, total + num[curr])
        plus += 1
    if minus:
        minus -= 1
        dfs(curr+1, total - num[curr])
        minus += 1
    if multi:
        multi -= 1
        dfs(curr+1, total * num[curr])
        multi += 1
    if div:
        div -= 1
        dfs(curr+1, int(total / num[curr]))
        div += 1


dfs(1, num[0])  # 첫 번째 값 넣어서 시작
print(max_val)
print(min_val)
