# "연속된 수들"의 부분합
from operator import length_hint
import sys
input = sys.stdin.readline # 입력 가속

n, s = map(int, input().split()) # 수열의 길이 n, 합 s
nums = list(map(int, input().split())) # 수열

def subtotal(nums, s):
    if sum(nums) < s: # 모든 요소를 다 합쳐도 합이 s 이상 되지 않을 때
        return 0

    start, end = 0, 0
    length = 100001
    total = 0
    while start < n:
        if total >= s:
            length = min(length, end - start)
            total -= nums[start]
            start += 1
        else:
            if end == n: # start를 증가시켜도 total이 더 줄어들기 때문에, 바로 반복문 탈출
                break
            total += nums[end]
            end += 1

    return length if length != 100001 else 0

print(subtotal(nums, s))