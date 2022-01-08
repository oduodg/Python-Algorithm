import sys
input = sys.stdin.readline

T = int(input())
stack = []

# ( 이면 stack에 담고 , ) 이면 (를 pop
# 빈 stack인데 )가 들어오면 -> NO
# 검사가 다 끝나고 빈 stack이면 -> YES , 빈 스택이 아니면 -> NO

def is_vps(ps):
    stack = []
    for i in range(len(ps)):
        if not stack and ps[i] == ')':
            return False
        elif ps[i] == '(':
            stack.append('(')
        elif ps[i] == ')':
            stack.pop()
    if not stack: # 스택이 비어있으면
        return True
    else:
        return False

for _ in range(T):
    ps = input()
    if is_vps(ps):
        print('YES')
    else:
        print('NO')