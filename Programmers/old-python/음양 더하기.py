def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]: # True이면
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# Test Case
abs1 = [4, 7, 12]
signs1 = [True, False, True]

abs2 = [1, 2, 3]
signs2 = [False, False, True]

print(solution(abs1, signs1))
print(solution(abs2, signs2))
