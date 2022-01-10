# 음수, 0, 양수, 최솟값, 최댓값 -> 반드시 확인해볼 엣지케이스 명심 !
import sys, collections
input = sys.stdin.readline # 입력 가속

q = collections.deque()
def queue(command):
    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])

N = int(input()) # 명령의 개수
for _ in range(N):
    command = input().split()
    queue(command)