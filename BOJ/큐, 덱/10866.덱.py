import sys, collections
input = sys.stdin.readline # 입력 가속
n = int(input()) # 명령의 수
deque = collections.deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deque.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)