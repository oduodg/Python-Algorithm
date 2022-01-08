import sys
input = sys.stdin.readline # 입력 가속

N = int(input())
answer = sorted(list(str(N)), reverse=True)
answer = int(''.join(answer))
print(answer)