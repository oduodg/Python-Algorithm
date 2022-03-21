import sys, collections
input = sys.stdin.readline

str = input().rstrip()  # 문자열
m = int(input())  # 명령어의 개수
left = list(str) # 왼쪽 스택
right = collections.deque() # 오른쪽 큐

for _ in range(m):
    cmd = input().rstrip()
    if cmd[0] == 'L': # 커서 왼쪽으로 이동
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D': # 커서 오른쪽으로 이동
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B': # 커서 왼쪽 문자 삭제
        if left:
            left.pop()
    elif cmd[0] == 'P': # 커서 왼쪽에 문자 추가
        left.append(cmd[2])

left.extend(right)
print(''.join(left))