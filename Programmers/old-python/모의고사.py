from collections import deque
import math

def solution(answers):

    num1 = deque([1,2,3,4,5] * math.ceil((len(answers)/5)))
    num2 = deque([2,1,2,3,2,4,2,5] * math.ceil((len(answers)/8)))
    num3 = deque([3,3,1,1,2,2,4,4,5,5] * math.ceil((len(answers)/10)))

    score1 = 0
    score2 = 0
    score3 = 0

    for answer in answers:
        if answer == num1.popleft():
            score1 += 1
        if answer == num2.popleft():
            score2 += 1
        if answer == num3.popleft():
            score3 += 1
    
    result = []
    scores = [score1, score2, score3]
    for i in range(len(scores)):
        if(scores[i] == max(scores)):
            result.append(i+1)
            
    
    return sorted(result)

# Test Case
answers1 = [1,2,3,4,5]
answers2 = [1,3,2,4,2]

print(solution(answers1))
print(solution(answers2))