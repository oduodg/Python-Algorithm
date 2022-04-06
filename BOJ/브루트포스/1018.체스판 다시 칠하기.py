n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input()))

result = []

# 8 x 8 체스판 만들기
for i in range(n-7):
    for j in range(m-7):
        startB = 0
        startW = 0
        # 체스판 검사
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 인덱스 합이 짝수인 경우 -> 시작 알파벳과 같은 알파벳이어야함
                if (a+b) % 2 == 0:
                    # B로 시작하는 경우
                    if chess[a][b] != 'B':
                        startB += 1
                    # W로 시작하는 경우
                    elif chess[a][b] != 'W':
                        startW += 1
                # 인덱스 합이 홀수인 경우 -> 시작 알파벳과 다른 알파벳이어야함
                else:
                    # B로 시작하는 경우
                    if chess[a][b] != 'W':
                        startB += 1
                    # W로 시작하는 경우
                    elif chess[a][b] != 'B':
                        startW += 1
        result.append(min(startB, startW))

print(min(result))