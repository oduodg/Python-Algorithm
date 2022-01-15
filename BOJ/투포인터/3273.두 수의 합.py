import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 수열의 크기
nums = list(map(int, input().split())) # 수열
x = int(input())

nums.sort()
cnt = 0
i, j = 0, len(nums)-1
while i < j:
    if nums[i] + nums[j] == x:
        cnt += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] > x:
        j -= 1
    else:
        i += 1
print(cnt)