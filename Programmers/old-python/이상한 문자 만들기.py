def solution(s):
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i].isalpha(): 
            if cnt % 2 == 0:
                s[i] = s[i].upper()
                cnt += 1
            else:
                s[i] = s[i].lower()
                cnt += 1
        else: # 공백문자 일 때
            cnt = 0

    return ''.join(s)

# Test Case
s = "try hello world"

print(solution(s))