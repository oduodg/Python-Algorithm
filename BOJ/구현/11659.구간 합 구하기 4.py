import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
""" # 시간 초과
for _ in range(m):
    start, end = map(int, input().split())
    print(sum(nums[start-1:end]))
"""
sec = [0, nums[0]] + [0] * (n-1)
for i in range(1, n):
    sec[i+1] = sec[i] + nums[i]  # 처음부터 해당 숫자까지의 구간의 합을 미리 구해놓는다.
for _ in range(m):
    start, end = map(int, input().split())
    print(sec[end]-sec[start-1])  # 끝 구간에서 start 직전까지의 구간의 합을 빼준다.
