import sys
input = sys.stdin.readline

n = int(input())  # 수열 seq의 크기 n
seq = [0] + list(map(int, input().split()))  # 수열 seq, index 맞추기 귀찮아서 앞에 0 추가함
m = int(input())  # 질문의 개수 m

# dp 풀이
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for s in range(n, 0, -1):  # 뒤에서부터 거꾸로 해야됨. 왜냐면 아래 elif문에서 [s+1]행 값을 알아야하기때문에
    for e in range(s, n+1):
        if e == s:  # 숫자가 1개인 경우(처음 인덱스와 끝 인덱스가 같으면)
            dp[s][e] = 1  # 무조건 참(팰린드롬)
        elif e == s+1 and seq[s] == seq[e]:  # 숫자가 2개인 경우 두 숫자가 같아야 팰린드롬
            dp[s][e] = 1
        elif seq[s] == seq[e] and dp[s+1][e-1]:  # 시작 숫자와 끝 숫자가 같고 중간 수열이 팰린드롬이면
            dp[s][e] = 1  # 얘도 팰린드롬임 -> yxxxxy (시작과 끝이 y로 같고 중간 xxxx는 팰린드롬인 수열)

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])

""" # 시간 초과
for _ in range(m):
    s, e = map(int, input().split())
    flag = True  # 팰린드롬 확인
    while s != int((e+s)//2):
        if seq[s] != seq[e]:
            flag = False
            break
        else:
            s += 1
            e -= 1

    if flag:
        print(1)
    else:
        print(0)
"""
