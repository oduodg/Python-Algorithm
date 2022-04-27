n = int(input()) # 첫 번째 장대에 쌓인 원판의 개수

result = []
def hanoi(n, start, end, mid):
    if n == 1: # 원판이 1개인 경우
        result.append([start, end]) # start에서 end로 옮기면 완료
    else:
        # 맨 아래 가장 큰 원판을 제외한 원판 n-1개를 start에서 mid로 옮김
        hanoi(n-1, start, mid, end)
        # 남은 1개의 원판(제일 큰 원판)을 start에서 end로 옮김
        result.append([start, end])
        # mid에 옮겨놨던 원판 n-1개를 mid에서 end로 옮김
        hanoi(n-1, mid, end, start)

    return result

result = hanoi(n, 1, 3, 2)
print(len(result))
for res in result:
    print(*res)