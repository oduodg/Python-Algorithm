import sys
input = sys.stdin.readline
# 리스트로 변환해서 입력받음
string = list(input().rstrip())
bomb = list(input().rstrip())

stack = []
for letter in string:
    stack.append(letter)
    if stack[-1] == bomb[-1]:
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if stack == []:
    print('FRULA')
else:
    print(''.join(stack))