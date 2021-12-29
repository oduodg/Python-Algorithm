def solution(a, b):
    answer = 0
    if a == b:
        return a
    else:
        small = min(a,b)
        big = max(a,b)
        for i in range(small, big+1):
            answer += i
        return answer

def solution2(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a # swap
    return sum(range(a, b+1))

# Test Case
print(solution(3, 5)) # 12
print(solution(3, 3)) # 3
print(solution(5, 3)) # 12


print(solution2(3, 5)) # 12
print(solution2(3, 3)) # 3
print(solution2(5, 3)) # 12