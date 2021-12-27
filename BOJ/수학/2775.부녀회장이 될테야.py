import sys
input = sys.stdin.readline # 입력 가속
''' # 시간 초과
def count_people(k, n):
    result = 0
    if k == 0:
        return n
    for i in range(1, n+1):
        result += count_people(k-1, i)
    
    return result

t = int(input()) # test case의 개수
for _ in range(t):
    k = int(input())
    n = int(input())
    print(count_people(k, n))

'''

t = int(input())
for _ in range(t):
    answer = [i for i in range(1, 15)] # 제한 조건 n <= 14 
    k = int(input())
    n = int(input())

    if k == 0:
        print(answer[n-1])
    elif n == 1:
        print(1)
    else:
        for _ in range(k):
            for i in range(1, n):
                answer[i] += answer[i-1]
    
        print(answer[n-1])