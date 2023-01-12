def solution(citations):
    n = len(citations)
    citations = sorted(citations)
    
    for i in range(n):
        if citations[i] >= n-i: # citations[i]는 i번 인용된 횟수, n-i는 인용된 논문의 개수
            return n-i

    return 0 # 0일 때 빼먹지 말기

# Test Case
TC1 = [3, 0, 6, 1, 5]

print(solution(TC1))