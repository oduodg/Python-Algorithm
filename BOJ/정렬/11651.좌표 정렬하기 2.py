import sys
input = sys.stdin.readline

N = int(input())

answer = []
for _ in range(N):
    x, y = map(int, input().split())
    answer.append([x,y])

answer.sort(key=lambda x:(x[1],x[0]))
for i in range(len(answer)):
    print(answer[i][0], answer[i][1])