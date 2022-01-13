import sys, math
input = sys.stdin.readline # 입력 가속

''' # 시간초과
a, b, v = map(int, input().split())
location = 0
days = 0
while location < v:
    days += 1
    location += a
    if location >= v:
        break
    else:
        location -= b

print(days)
'''
a, b, v = map(int, input().split())
# (a-b) * days + a = v , 마지막 날은 올라가고 떨어지지 않으므로 +a를 해주어야 함
days = math.ceil((v-a) / (a-b)) + 1 # 소수점 이하는 날짜로 보면 하루가 걸린 것과 같으므로 올림을 해주고, 마지막 날 a만큼 올라간 하루 +1를 더해준다.
print(days)