import sys
input = sys.stdin.readline
n = int(input())  # 회의의 수 n

meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

# 끝나는 시간이 빠른 순으로 정렬
# 끝나는 시간이 같다면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

start = meetings[0][0]
end = meetings[0][1]
cnt = 1  # 맨 처음 회의에 해당하는 meetings[0] count해서 1로 초기화
for i in range(1, n):
    start = meetings[i][0]
    if end <= start:
        cnt += 1
        end = meetings[i][1]

print(cnt)
