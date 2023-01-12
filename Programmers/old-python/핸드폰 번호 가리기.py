def solution(phone_number):
    answer = "*" * (len(phone_number)-4) + phone_number[-4:]
    return answer

# Test Case
TC1 = "01033334444"
TC2 = "027778888"
TC3 = "01234567890123456789"


print(solution(TC1))
print(solution(TC2))
print(solution(TC3))