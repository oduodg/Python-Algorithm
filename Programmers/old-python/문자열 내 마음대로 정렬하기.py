def solution(strings, n): # n번째 글자를 기준으로 오름차순 정렬 -> key함수의 lambda
    return sorted(sorted(strings), key=lambda x:(x[n]))
    
# Test Case
print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))