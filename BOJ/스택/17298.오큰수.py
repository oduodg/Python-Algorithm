import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())  # 수열 A의 크기
A = list(map(int, input().split()))  # 수열 A
answer = [-1] * n
stack = [[A[0], 0]]
for i in range(1, n):
    if stack[-1][0] >= A[i]:
        stack.append([A[i], i])
    else:
        while stack and stack[-1][0] < A[i]:
            num, idx = stack.pop()
            answer[idx] = A[i]
        stack.append([A[i], i])

for oh_big in answer:
    print(oh_big, end=' ')
