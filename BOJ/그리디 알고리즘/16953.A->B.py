# Algorithm(수학적 사고)
# 거꾸로 생각을 해서 B를 A로 바꾼다고 생각해보자.
# 1. b가 짝수이면 그 전에 2를 곱한 것이다.
# 2. b의 일의 자리가 1이라면 그 전에 1을 오른쪽에 추가한 것이다.
# 위 두가지 경우에 모두 해당이 되지 않는다면 A를 B로 바꿀 수 없다. 즉, -1을 출력한다.

'''
a, b = map(int, input().split())

ans = 1
while a < b:
    if b == a: # a를 b로 바꾼 경우
        break
    elif b % 2 == 0: # b가 짝수인 경우
        b //= 2
        ans += 1
    elif b % 10 == 1: # b의 일의 자리가 1인 경우
        b //= 10
        ans += 1
    else:
        ans = -1
        break

if b != a:
    ans = -1

print(ans)
'''

# Algorithm(그리디, bfs)
# 큐(덱)를 이용해서 풀이한다. 
# 먼저 큐에 [a, 1]을 넣어준다. (1은 필요한 연산 count)
# while문으로 큐가 empty될 때까지 popleft를 한다.
# popleft한 값에 2를 곱한 값이 b보다 작다면 큐에 넣어준다.
# popleft한 값에 1을 오른쪽에 추가한 값이 b보다 작다면 큐에 넣어준다.
# a == b를 찾으면 break
# b로 바꿀 수 있다면 cnt를 출력하고 그렇지 않다면 -1을 출력한다.

from collections import deque

a, b = map(int, input().split())
q = deque([[a, 1]])

while q:
    cur, cnt = q.popleft()
    if cur == b:
        break
    
    if cur * 2 <= b: q.append([cur * 2, cnt + 1])
    if int(str(cur) + '1') <= b: q.append([int(str(cur) + '1'), cnt + 1])

if cur == b:
    print(cnt)
else:
    print(-1)