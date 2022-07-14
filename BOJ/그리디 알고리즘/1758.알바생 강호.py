import sys
input = sys.stdin.readline

n = int(input()) # 스타박스 앞에 서 있는 사람의 수 
tip = []
ans = 0

for _ in range(n):
    tip.append(int(input()))

tip.sort() # 팁이 낮은 순으로 정렬

i = 0
while tip:
    tmp = tip.pop() - i
    if tmp >= 0:
        ans += tmp
    i += 1

print(ans)

# Algorithm: 팁이 높은 순서대로 먼저 입장하면 된다.
# 스택을 사용해서 팁이 낮은 순으로 정렬했다. pop하면 팁이 높은 것 먼저 순서대로 나오게 된다.
# 음수인 경우 팁을 주지 않으므로 조건문 설정을 잊지않고 해야한다. (처음에 까먹음ㅎㅎ)