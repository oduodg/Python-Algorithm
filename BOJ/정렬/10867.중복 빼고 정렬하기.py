import sys
input = sys.stdin.readline
n = int(input()) # n개의 정수
arr = list(map(int, input().split()))
for num in sorted(set(arr)):
    print(num, end=" ")