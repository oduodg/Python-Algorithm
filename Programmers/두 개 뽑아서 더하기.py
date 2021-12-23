def solution(numbers):
    answer = []

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)
    
    return sorted(answer)

# Test Case
TC1 = [2,1,3,4,1]
TC2 = [5,0,2,7]

print(solution(TC1))
print(solution(TC2))