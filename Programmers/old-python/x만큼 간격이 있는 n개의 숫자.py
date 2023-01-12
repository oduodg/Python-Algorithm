def solution(x, n):
    answer = []
    add = x
    while len(answer) != n:
        answer.append(x)
        x += add
    return answer

# Test Case
print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))