import sys
input = sys.stdin.readline  # 입력 가속
k = int(input())
x = 1
for _ in range(k):
    line = list(map(int, input().split()))
    n = line[0]
    score = line[1:]
    score.sort(reverse=True)
    Max = score[0]
    Min = score[-1]
    gap = max([score[i]-score[i+1] for i in range(n-1)])
    print("Class", x)
    x += 1
    print("Max", Max, end=', ')
    print("Min", Min, end=', ')
    print("Largest gap", gap)
