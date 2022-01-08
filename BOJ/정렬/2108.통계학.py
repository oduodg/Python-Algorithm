import sys, collections
input = sys.stdin.readline # 입력 가속

N = int(input()) # 수의 개수

nums = []
for _ in range(N):
    num = int(input())
    nums.append(num)

print(round(sum(nums)/N)) # 산술평균
print(sorted(nums)[N//2]) # 중앙값
# 시간초과 # print(max(nums, key=nums.count)) # 최빈값
cnt_nums = collections.Counter(sorted(nums)).most_common()
if len(cnt_nums) > 1:
    if cnt_nums[0][1] == cnt_nums[1][1]:
        print(cnt_nums[1][0]) # 두 번째로 작은 값 출력
    else:
        print(cnt_nums[0][0])
else:
    print(cnt_nums[0][0])
print(max(nums)-min(nums)) # 범위