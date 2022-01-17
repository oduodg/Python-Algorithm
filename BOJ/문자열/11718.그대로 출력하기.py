import sys
input = sys.stdin.readline # 입력 가속

while True:
    try:
        print(input())
    except EOFError:
        break