def solution(s):
    answer = ""
    numDic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    word = ""
    for i in range(len(s)):
        if s[i].isalpha(): # 알파벳이면
            word += s[i]
            if word in numDic:
                answer += str(numDic[word])
                word = ""
        else: # 숫자이면
            answer += str(s[i]) # 숫자 그대로 추가
    
    return int(answer)

def solution2(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    for key, value in num_dic.items():
        s = s.replace(key, value)
    return int(s)

# Test Case
TC1 = "one4seveneight"
TC2 = "23four5six7"
TC3 = "2three45sixseven"
TC4 = "123"

print(solution(TC1))
print(solution(TC2))
print(solution(TC3))
print(solution(TC4))

print(solution2(TC1))
print(solution2(TC2))
print(solution2(TC3))
print(solution2(TC4))