# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다.
# 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 한다.
# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 체육수업을 들을 수 있는 학생의 최댓값을 return

# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost) # 여벌 체육복이 있는 학생들
    _lost = set(lost) - set(reserve) # 자기 체육복이 없는 학생들

    for i in _reserve:
        if i-1 in _lost: # 앞번호에게 빌려주기
            _lost.remove(i-1)
        elif i+1 in _lost: # 뒷번호에게 빌려주기
            _lost.remove(i+1)
        
    return n - len(_lost)
    
# Test Case
n1 = 5
lost1 = [2,4]
reserve1 = [1,3,5]

n2 = 5
lost2 = [2,4]
reserve2 = [3]

n3 = 3
lost3 = [3]
reserve3 = [1]

print(solution(n1, lost1, reserve1)) # 5
print(solution(n2, lost2, reserve2)) # 4
print(solution(n3, lost3, reserve3)) # 2