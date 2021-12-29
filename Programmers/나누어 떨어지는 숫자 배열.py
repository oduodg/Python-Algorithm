def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if not answer: # answer이 비어있으면
        return [-1]
    return sorted(answer)

def solution2(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

# Test Case
ar1 = [5,9,7,10]
ar2 = [2,36,1,3]
ar3 = [3,2,6]

print(solution(ar1, 5)) # [5, 10]
print(solution(ar2, 1)) # [1, 2, 3, 36]
print(solution(ar3, 10)) # [-1]


print(solution2(ar1, 5)) # [5, 10]
print(solution2(ar2, 1)) # [1, 2, 3, 36]
print(solution2(ar3, 10)) # [-1]