def solution(array, commands):
    result = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        num = sorted(array[i-1:j])
        result.append(num[k-1])
    return result

# Test Case
array1 = [1, 5, 2, 6, 3, 7, 4]
commands1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array1, commands1))