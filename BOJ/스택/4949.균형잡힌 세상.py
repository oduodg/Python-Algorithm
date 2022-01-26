import sys
input = sys.stdin.readline # 입력 가속
def solution(line):
    stack = []
    for i in range(len(line)):
        if line[i] == '(':
            stack.append('(')
        elif line[i] == ')':
            if not stack:
                return "no"
            else:
                pop = stack.pop()
                if pop != '(':
                    return "no"
        elif line[i] == '[':
            stack.append('[')
        elif line[i] == ']':
            if not stack:
                return "no"
            else:
                pop = stack.pop()
                if pop != '[':
                    return "no"
    if stack:
        return "no"
    else:
        return "yes"

while True:
    line = input().rstrip()
    if line == '.':
        break
    print(solution(line))