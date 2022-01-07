import sys
input = sys.stdin.readline

T = int(input())

''' # 메모리 초과
answer = []
for _ in range(T):
    num = int(input())
    answer.append(num) # for문 안에서 append를 사용하게 되면 메모리 재할당이 이루어져 메모리를 효율적으로 사용하지 못한다.

for num in sorted(answer):
    print(num)
'''

answer = [0] * 10001 # 미리 최대 크기의 배열을 만든다.
# 배열의 인덱스가 가리키는 요소에는 각 숫자의 개수가 들어간다.
for _ in range(T):
    answer[int(input())] += 1

for i in range(10001):
    if answer[i] != 0:
        for _ in range(answer[i]):
            print(i)