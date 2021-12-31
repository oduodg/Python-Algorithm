def solution(n):
    if int(n**0.5) == n**0.5:
        return (n**0.5 +1)**2
    else:
        return -1

# Test Case
print(solution(121))
print(solution(3))