import sys
input = sys.stdin.readline

t = int(input())  # 테스트 케이스의 수
for _ in range(t):
    n = int(input())  # 후보자의 수
    candi = []
    for i in range(n):
        candi.append(int(input()))  # 득표 수

    total = sum(candi)  # 총 득표 수
    winner = max(candi)  # 최다 득표자의 득표 수
    if candi.count(winner) > 1:
        print("no winner")
    else:
        if winner > total//2:
            print("majority winner", candi.index(winner)+1)
        else:
            print("minority winner", candi.index(winner)+1)
