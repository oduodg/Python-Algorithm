import itertools, math

def solution(nums):
    # 소수 판별 함수
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

    it = itertools.combinations(nums, 3)
    answer = 0
    for nums in it:
        if is_prime(sum(nums)):
            answer += 1
    return answer

# Test Case
print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))