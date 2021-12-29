def solution(n):
    for x in range(1, n):
        i = n % x
        if i == 1:
            return x
            
# Test Case
TC1 = 10
TC2 = 12

print(solution(TC1))
print(solution(TC2))