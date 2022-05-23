import sys
input = sys.stdin.readline
n = int(input())  # 일의 개수
work = list(map(int, input().split()))  # 일
s = set()
s.add(0)  # 자기 자신을 더해줘야 하므로 0을 추가

for work1 in work:
    for work2 in set(s):  # set(s)는 새로운 객체이므로, 앞에서 정의된 s에 대해서만 적용됨(set(s)는 for문을 돌면서 변하지 않음)
        tmp = (work1 + work2) % 7
        if tmp == 4:
            print('YES')
            exit()
        s.add(tmp)
print('NO')
