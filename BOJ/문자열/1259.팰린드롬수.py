def solution(n):
    j = -1
    for i in range(len(n)):
        if n[i] != n[j]:
            return 'no'
        j -= 1
    return 'yes'


while True:
    n = int(input())
    if n == 0:
        break
    else:
        n = list(map(int, str(n)))
        print(solution(n))
