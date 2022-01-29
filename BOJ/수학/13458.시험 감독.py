import sys, math
input = sys.stdin.readline # 입력 가속

n = int(input()) # 시험장의 개수
a = list(map(int, input().split())) # 응시자의 수
b, c = map(int, input().split()) # 감시할 수 있는 응시자의 수(총감독관, 부감독관)
cnt = 0

for i in range(len(a)):
    if a[i] - b <= 0:
        cnt +=1
    else:
        cnt += 1 + math.ceil((a[i] - b)/c)

print(cnt)