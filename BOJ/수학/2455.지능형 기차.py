station1 = list(map(int, input().split()))
station2 = list(map(int, input().split()))
station3 = list(map(int, input().split()))
station4 = list(map(int, input().split()))

st = [station1, station2, station3, station4]
cnt = 0
max_cnt = 0
for i in range(4):
    cnt -= st[i][0]
    cnt += st[i][1]
    max_cnt = max(cnt, max_cnt)

print(max_cnt)