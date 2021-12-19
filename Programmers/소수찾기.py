import itertools
import math

def solution(numbers):
    answer = []
    numbers = list(numbers)
    
    # 소수 판별 함수
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

    for i in range(1, len(numbers)+1):
        nPr = itertools.permutations(numbers,i)
        for item in nPr:
            number = int(''.join(item))
            if is_prime(number):
                answer.append(number)
    
    return len(set(answer))


# Test Case
TC1 = "17"
TC2 = "011"

print(solution(TC1))
print(solution(TC2))