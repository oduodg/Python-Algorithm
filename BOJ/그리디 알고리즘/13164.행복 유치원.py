import sys
input = sys.stdin.readline
n, k = map(int, input().split())
kids = list(map(int, input().split())) # 오름차순으로 입력됨

diff = [] # 바로 옆 원생과의 키 차이를 담을 배열

for i in range(n-1):
    diff.append(kids[i+1]-kids[i])

diff.sort()

for _ in range(k-1):
    diff.pop()

print(sum(diff))