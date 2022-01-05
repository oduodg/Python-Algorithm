def solution(x):
    div = sum(list(map(int, (list(str(x)))))) # str로 만든 후, 리스트 형태로 변환 -> 리스트 요소를 int형으로 다시 변환 후 모든 요소의 합
    if x % div == 0:
        return True
    else:
        return False

def solution2(x):
    return x % sum([int(c) for c in str(x)]) == 0
    # 더 간단하게, for문으로 str타입의 x를 int타입으로 하나씩 접근하기

# Test Case
print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))

print(solution2(10))
print(solution2(12))
print(solution2(11))
print(solution2(13))