# key:value를 이루는 딕셔너리를 이름:숫자 ,숫자:이름 2가지를 만들면 쉽다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # 포켓몬의 개수 n, 문제의 개수 m
pocketmon_num = {}
pocketmon_name = {}
for num in range(1, n+1):
    name = input().rstrip()  # 포켓몬 이름
    pocketmon_num[name] = num
    pocketmon_name[num] = name

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():  # 문제가 숫자인 경우
        print(pocketmon_name[int(q)])
    else:
        print(pocketmon_num[q])
