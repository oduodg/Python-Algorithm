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
