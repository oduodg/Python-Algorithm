import math
def solution(n): # 시간 초과
    def is_prime(x):
        # 2부터 x의 제곱근까지의 모든 수를 확인
        for i in range(2, int(math.sqrt(x))+ 1): 
            # x가 해당 수로 나누어 떨어진다면
            if x % i == 0:
                return False # 소수 아님
        return True # 소수임

    answer = 0
    for num in range(2, n+1):
        if is_prime(num): # 소수이면
            answer += 1
    return answer

def solution2(n): # 에라토스테네스의 체 -> 소수의 배수를 지워나감
    answer = 0
    cnt = [True] * (n+1)
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(n**0.5) +1):
        if cnt[i]: # 소수이면
            for j in range(i*2, n+1, i): # i의 배수들을 False로 변환
                cnt[j] = False
    for i in range(2, n+1): # 소수 개수 count
        if cnt[i]:
            answer += 1
    return answer

def solution3(n): # set을 활용한 에라토스테네스의 체
    num = set(range(2, n+1)) # 2부터 n+1까지의 집합
    for i in range(2, n+1): # 2부터 n까지 반복문
        if i in num: # 만약 i가 num 집합에 있으면
            num -= set(range(i*2, n+1, i)) # i의 배수는 num에서 제외
    return len(num)

# Test Case
print(solution(10))
print(solution(5))

print(solution2(10))
print(solution2(5))

print(solution3(10))
print(solution3(5))