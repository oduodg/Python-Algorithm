import collections

def solution(priorities, location):
    q = collections.deque([(priority, idx) for (idx, priority) in enumerate(priorities)])
    answer = 0

    while q:
        # max(q)는 q의 요소 중 (i, j) 에서 i가 가장 높은 요소를 반환하므로, i가 가장 높은(우선순위가 가장 높은) 요소의 [0]은 즉 i(우선순위)를 반환
        paper = q.popleft() # 맨 앞의 문서를 pop
        if q and paper[0] < max(q)[0]: # 중요도가 낮다면 (마지막 문서를 인쇄할 때는 q가 비어있으므로 q를 조건문에 추가해주어야 에러가 안남)
            q.append(paper) # 맨 뒤에 다시 삽입
        else:
            answer += 1
            if paper[1] == location:
                break

    return answer

# Test Case
TC1 = [2, 1, 3, 2]
loc1 = 2

TC2 = [1, 1, 9, 1, 1, 1]
loc2 = 0

print(solution(TC1, loc1))
print(solution(TC2, loc2))