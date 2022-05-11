import sys
input = sys.stdin.readline # 입력 가속
t = int(input()) # 테스트 케이스의 수
for _ in range(t):
    n = int(input()) # 의상의 수
    clothes = {}
    for _ in range(n):
        name, type = map(str, input().split()) # 의상의 이름과 종류
        if type not in clothes:
            clothes[type] = 2
        else:
            clothes[type] += 1
    answer = 1
    for key, value in clothes.items():
        answer *= value
    print(answer-1)