n, k = map(int, input().split())
def is_prime(n, k):
    num = [True] * 1001
    cnt = 0
    for i in range(2, n+1):
        for i in range(i, n+1, i): # p와 p의 배수 지우기
            if num[i]:
                cnt += 1
                num[i] = False
                if cnt == k:
                    return i
print(is_prime(n, k))