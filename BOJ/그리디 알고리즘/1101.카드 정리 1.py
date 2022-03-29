import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 박스의 개수 n, 카드 색상의 개수 m
box = [0] * n
not_empty_box = [] # 비어있지 않은 박스 카운트
for i in range(n):
    box[i] = list(map(int, input().split()))
    # 카드가 1개 이상 존재하는(빈 박스 제외) 박스 카운트
    color_cnt = 0 # 카드 색상의 개수 카운트
    colors = []
    for color, card in enumerate(box[i]):
        if card == 0:
            continue
        else:
            color_cnt += 1
            colors.append(color) # 해당 색깔의 인덱스 추가

    not_empty_box.append((color_cnt, colors))

ans = n
# n개의 상자를 전부 한번씩 조커 상자로 가정하고 최소 이동 횟수 구하기
for i in range(n):
    cnt = 0 # 최소 이동 횟수 카운트
    jocker = not_empty_box[0] # 조커 상자 지정
    not_empty_box.remove(jocker) # 조커 상자 제거
    checked = [False] * m # 해당 색깔이 이전 박스에서 나왔는지 체크하기 위한 배열
    for color_cnt, colors in not_empty_box:
        if color_cnt > 1: # 두가지 색깔 이상이면
            cnt += 1 # 무조건 카드 이동이 필요함.
        elif color_cnt == 1:
            color = colors[0]
            if not checked[color]: # 처음 나오는 색깔이면
                checked[color] = True # 해당 박스에서 그 색깔을 모아준다. (카드를 이동시킬 필요 x)
            else:
                cnt += 1
    ans = min(ans, cnt)
    not_empty_box.append(jocker) # 다음 경우의 수를 위해 조커 상자 다시 추가

print(ans)