import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())  # 기타의 개수 n
guitars = []
for _ in range(n):
    sn = input().rstrip()
    # 숫자들의 합
    i = sum(map(int, [str for str in list(sn) if 48 <= ord(str) <= 57]))
    guitars.append([sn, len(sn), i])
guitars.sort(key=lambda x: (x[1], x[2], x[0]))  # 길이 -> 합 -> 사전순 정렬
for sn, len, i in guitars:
    print(sn)
