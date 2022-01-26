import sys
n = int(sys.stdin.readline())

if '0' not in str(n): # 30의 배수이려면 무조건 '0'으로 끝나야함.
    print(-1)
else:
    str_n = list(str(n))
    str_n.sort(reverse=True) # 가장 큰 수로 만듬
    n = list(map(int, str_n))
    if sum(n) %3 != 0: # 각 자리의 합이 3의 배수이면 그 수는 3의 배수임.
        print(-1)
    else:
        print(''.join(str_n))