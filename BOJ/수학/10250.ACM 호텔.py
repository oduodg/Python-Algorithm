import sys
input = sys.stdin.readline # 입력 가속

# 선호 순서: 101 -> 201 -> 301 .. -> 102 -> 202 -> 302 -> ..

t = int(input()) # test case의 개수

for _ in range(t):
    h, w, n = map(int, input().split()) # 층 수, 방 수, n 번째 손님  
    if n % h == 0: # 6의 배수이면
        if n//h < 10:
            print(int(str(h) + '0' + str(n//h)))
        else:
            print(int(str(h) + str(n//h)))
    else:
        if n//h + 1 < 10:
            print(int(str(n%h) + '0' + str(n//h +1)))
        else:
            print(int(str(n%h) + str(n//h +1)))