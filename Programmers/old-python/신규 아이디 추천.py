import re

def solution(new_id):
    answer = ''
    answer = new_id.lower() # 1단계
    answer = re.sub('[^a-z\d\-\_\.]', '', answer) # 2단계
    answer = re.sub('\.\.+', '.', answer) # 3단계
    answer = re.sub('^\.|\.$', '', answer) # 4단계
    if answer == '': # 5단계
        answer = 'a'
    if len(answer) >= 16: # 6단계
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]
    while len(answer) < 3: # 7단계
        answer = answer + answer[-1]
    return answer

# Test Case

TC1 = "...!@BaT#*..y.abcdefghijklm"
TC2 = "z-+.^."
TC3 = "=.="
TC4 = "123_.def"
TC5 = "abcdefghijklmn.p"

print(solution(TC1)) # "bat.y.abcdefghi"
print(solution(TC2)) # "z--"
print(solution(TC3)) # "aaa"
print(solution(TC4)) # "123_.def"
print(solution(TC5)) # "abcdefghijklmn"