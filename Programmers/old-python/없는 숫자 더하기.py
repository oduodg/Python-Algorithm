def solution(numbers):
    total = sum([num for num in range(0,10)])
    return total - sum(numbers)

# Test Case
TC1 = [1,2,3,4,6,7,8,0]
TC2 = [5,8,4,0,6,7,9]

print(solution(TC1))
print(solution(TC2))