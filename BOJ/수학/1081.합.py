import copy
l, u = map(int, input().split())

def solution(n):
    m = copy.deepcopy(n)
    digit = 1
    ans = 0
    while n != 0:
        s, r = divmod(n, 10)
        ans += 45 * (s + 1) * digit
        ans -= sum([i for i in range(r+1, 10)]) * digit
        if digit != 1:
            ans -= r * ((n*digit + (digit-1) - m))
        n = n//10
        digit *= 10    
    return ans

print(solution(u) - solution(l) + sum(int(i) for i in str(l)))

# 11 -> 19: n=11, s=1, r=1
# 일의자리: 45 * (1+1) * 1 // -sum(range(2,10)) * 1
# 90 - 44 = 46

# 1x -> 9x: n=1, s=0, r=1
# 십의자리: 45 * (0+1) * 10 // -sum(range(2,10)) * 10
# 12~19의 십의자리 1 * (19-11)개 빼주어야함
# 450 - 440 - 8 = 2


# 137 -> 139: n=137, s=13, r=7
# 일의자리: 45 * (13+1) * 1 // -8, -9

# 13x -> 19x: n=13, s=1, r=3
# 십의자리: 45 * (1+1) * 10 // -sum(range(4,10)) * 10
# 138, 139의 십의자리 3(=r) *(139-137)개 빼주어야함
# 여기서 139는 n*digit + (digit-1)

# 1xx -> 9xx: n=1, s=0, r=1
# 백의자리: 45 * (0+1) * 100 // -sum(range(2,10)) * 100
# 138~199의 백의자리 1(=r) *(199-137)개 빼주어야함
# 여기서 199는 n*digit + (digit-1)
