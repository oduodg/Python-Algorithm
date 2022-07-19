import sys
input = sys.stdin.readline
n = int(input()) # 크레인의 대수
limit = list(map(int, input().split())) # 크레인의 무게 제한
m = int(input()) # 박스의 개수
box = list(map(int, input().split())) # 박스의 무게
time = 0 # 걸리는 시간 

# 모든 박스를 배로 옮길 수 없는 경우
if max(box) > max(limit):
    print(-1)
    sys.exit()


# 무게 제한이 높은 크레인에 무게가 무거운 박스를 먼저 실어야 함.
limit.sort(reverse=True)
box.sort(reverse=True)

while box:
    for i in range(n): # 크레인
        for j in range(len(box)): # 박스
            if box[j] <= limit[i]: # 크레인에 박스를 실을 수 있으면
                del box[j] # 박스를 옮김
                break # 다음 크레인으로   
    time += 1

print(time)