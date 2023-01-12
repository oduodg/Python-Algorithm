import math

def solution(progresses, speeds):
    complete = [] # 각 기능별로 기능개발 완료에 소요되는 일 수
    for i in range(len(progresses)):
        complete.append(math.ceil((100 - progresses[i]) / speeds[i]))

    result = []
    cnt = 1 # 배포될 기능 수 count
    time = complete[0]
    for i in range(1, len(complete)):
        if time >= complete[i]:
            cnt += 1
        else:
            result.append(cnt) # 전에 배포된 기능 수
            time = complete[i]
            cnt = 1
    result.append(cnt) # for문 종료 후 마지막 cnt 추가

    return result


# Test Case
pr1 = [93, 30, 55]
sp1 = [1, 30, 5]

pr2 = [95, 90, 99, 99, 80, 99]
sp2 = [1, 1, 1, 1, 1, 1]

print(solution(pr1, sp1))
print(solution(pr2, sp2))