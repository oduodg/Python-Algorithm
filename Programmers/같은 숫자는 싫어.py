def solution(arr):
    answer = []
    for num in arr:
        if answer == []:
            answer.append(num)
        if answer[-1] != num:
            answer.append(num)
    return answer

# Test Case
arr1 = [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]

print(solution(arr1))
print(solution(arr2))