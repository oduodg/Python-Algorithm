
def solution(s):
    result = []

    # 예외처리
    if len(s) == 1:
        return 1
    
    for i in range(1, (len(s)//2)+1): # 절반 이상 자르는 것은 압축이 안되므로 무의미함.
        comp = '' # 압축한 문자열을 담을 변수
        cnt = 1 # count
        tmp = s[:i] # 한 뭉치를 담을 변수

        for j in range(i, len(s), i): # 자를 단위 i만큼 뛰면서 반복문 실행
            if tmp == s[j:j+i]: # 다음 뭉치와 일치하면
                cnt += 1 # count up
            else:
                if cnt >= 2: # 앞 뭉치가 2번 이상 반복되었다면
                    comp = comp + str(cnt) + tmp
                else: 
                    comp = comp + tmp
                tmp = s[j:j+i] # 다음 뭉치로 
                cnt = 1 # count 1로 초기화

        # 마지막 뭉치에 대해서 처리
        if cnt >= 2:
            comp = comp + str(cnt) + tmp
        else:
            comp = comp + tmp

        result.append(len(comp))
    
    return min(result)
        

# Test Case
TC1 = "aabbaccc"
TC2 = "ababcdcdababcdcd"
TC3 = "abcabcdede"
TC4 = "abcabcabcabcdededededede"
TC5 = "xababcdcdababcdcd"

print(solution(TC1))
print(solution(TC2))
print(solution(TC3))
print(solution(TC4))
print(solution(TC5))