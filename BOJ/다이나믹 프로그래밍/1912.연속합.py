'''
n = int(input()) # 정수 n
nums = list(map(int, input().split())) # n개의 정수로 이루어진 수열
answer = nums[0]
for start in range(len(nums)-1):
    for end in range(start, len(nums)):
        answer = max(sum(nums[start:end+1]), answer)
print(answer)
'''

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    arr[i] = max(arr[i], arr[i-1] + arr[i])
print(max(arr))