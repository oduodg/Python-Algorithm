import sys
input = sys.stdin.readline # 입력 가속

M, N = map(int, input().split())

nums = set(range(2, N+1))
for i in range(2, N+1):
    if i in nums:
        nums -= set(range(i*2, N+1, i))
nums -= set(range(1, M))
for num in sorted(nums): # 집합은 순서를 보장해주지 않으므로 꼭 sorted로 순서대로 정렬해주어야 함. -> 백준에서 틀리게됨
    print(num)