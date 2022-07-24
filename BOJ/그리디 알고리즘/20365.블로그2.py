import sys
input = sys.stdin.readline
n = int(input())
color = list(input().rstrip())

blue = 0
red = 0
prev = color[0]
for i in range(1, n):
    if color[i] != prev: # 다음 색이 달라진다면
        if prev == "B":
            blue += 1
        else:
            red += 1

    prev =  color[i]
    
    if i == n-1: # 마지막 색깔
        if color[i] == "B":
            blue += 1
        else:
            red += 1

print(min(blue, red) + 1)