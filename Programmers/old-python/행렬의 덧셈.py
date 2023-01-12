def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)        
    return list(answer)

def solution2(arr1, arr2):
    answer = [[c+d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)] 
    # zip(arr1, arr2) => TC1: ([1,2], [3,4]), ... / a = [1,2], b = [3, 4]
    # zip(a, b) => TC1: (1,3), ... / c = 1, d = 3
    return answer

# Test Case
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))

print(solution2([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution2([[1],[2]], [[3],[4]]))