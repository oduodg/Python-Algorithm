def solution(prices):

    answer = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    answer.append(0) # 마지막 가격은 0초이므로 0 추가

    return answer

# Test Case
TC1 = [1,2,3,2,3]

print(solution(TC1))