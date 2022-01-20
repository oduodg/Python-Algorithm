n = int(input())
# 각 자연수의 분해합을 구한다.

def solution(n):
    for i in range(1, n+1):
        num_sum = i + sum(map(int, str(i))) # 분해합
        if num_sum == n:
            return i
    return 0

print(solution(n))