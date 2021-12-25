def solution(n): # 시간 초과
    answer = 0
    num = []
    if n == 1:
        return 1
    elif n == 2:
        return 2

    while n != 1:
        num.append(str(n % 3))
        n = n // 3
    num.append('1')
    num.reverse() # 뒤집기

    for i in range(len(num)):
        answer += (3**i) * int(num[i])
    
    return answer

def solution2(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3) # n을 3으로 나눈 몫(n)과 나머지(rest)
        answer += str(rest)
    
    answer = int(answer, 3) # answer를 3진법으로 변환(python의 int함수는 진법 변환을 지원한다.)

    return answer



# Test Case
n1 = 45
n2 = 125

print(solution(n1))
print(solution(n2))

print(solution2(n1))
print(solution2(n2))
