# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return

import itertools
import collections

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, itertools.product(*l)))
    return s.count(target)

def solution2(numbers, target): # bfs 풀이
    answer = 0
    queue = collections.deque()

    length = len(numbers)
    queue.append([-numbers[0], 0])
    queue.append([+numbers[0], 0])

    while queue:
        num, i = queue.popleft()
        if i+1 == length: # 노드의 끝까지 탐색한 경우
            if num == target:
                answer += 1
        else:
            queue.append([num - numbers[i+1], i + 1])
            queue.append([num + numbers[i+1], i + 1])
    
    return answer

# Test Case
numbers1 = [1,1,1,1,1]
target1 = 3

print(solution(numbers1, target1))
print(solution2(numbers1, target1))
