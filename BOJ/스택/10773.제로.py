import sys
input = sys.stdin.readline # 입력 가속

K = int(input()) # 정수의 개수

stack = []
for _ in range(K):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))