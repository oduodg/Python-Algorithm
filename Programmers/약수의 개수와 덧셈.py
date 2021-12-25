def solution(left, right):
    answer = [] # 약수의 개수를 담을 배열


    for num in range(left, right + 1):
        cnt = 2 # 1과 자기 자신
        if num == 1:
            cnt = 1
        for i in range(2, num // 2 + 1): # 숫자의 절반까지
            if num % i == 0: # 약수이면 
                if i * i == num: # 제곱근인 경우
                    cnt += 1
                elif num // i <= num // 2:
                    cnt += 1
                else:                
                    cnt += 2
        if cnt % 2 == 0: # 약수의 개수가 짝수이면
            answer.append(num)
        else:
            answer.append(-1*num)
    
    return sum(answer)

# Test Case
l1 = 13
r1 = 17

l2 = 24
r2 = 27

print(solution(l1, r1))
print(solution(l2, r2))