def solution(numbers):
    numbers = list(map(str, numbers)) # 숫자를 문자열로 변환
    numbers.sort(key=lambda x: x*3, reverse = True)
    
    return str(int(''.join(numbers)))
    
    

# Test Case
TC1 = [6, 10, 2]
TC2 = [3, 30, 34, 5, 9]
TC3 = [121, 12]
TC4 = [0, 0, 0]

print(solution(TC1))
print(solution(TC2))
print(solution(TC3))
print(solution(TC4))