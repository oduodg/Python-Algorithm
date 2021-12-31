def solution(n):
    n = list(str(n))
    n.reverse()
    n = list(map(int, n))
    return n

# Test Case
print(solution(12345))