import sys
input = sys.stdin.readline  # 입력 가속

min, max = map(int, input().split())
# max - min + 1 길이의 배열 선언
nums = [True] * (max - min + 1)


def solution(nums):
    cnt = max - min + 1
    for i in range(2, int(max**0.5)+1):  # 에라토스테네스의 체 -> 제곱근까지만 검사
        square = i*i  # 제곱수
        for j in range(((min-1)//square + 1) * square, max+1, square):  # 제곱수의 배수
            if nums[j-min]:
                nums[j-min] = False
                cnt -= 1
    return cnt


print(solution(nums))
