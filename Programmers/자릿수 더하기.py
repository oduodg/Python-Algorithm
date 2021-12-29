def solution(n):
    n = list(str(n))
    return sum(list(map(int, n)))

# Test Cae
print(solution(123))
print(solution(987))