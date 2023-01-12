def solution(n):
    n = list(str(n))
    return sum(list(map(int, n)))

# Test Case
print(solution(123))
print(solution(987))