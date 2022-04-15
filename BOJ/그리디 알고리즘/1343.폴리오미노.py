board = list(input())
board = board + ['.'] # 아래 for문에서 마지막 그룹 X를 확인하기위해 .을 추가한다.
polyA = 'AAAA'
polyB = 'BB'
result = []
cntX = 0
for i in range(len(board)):
    if board[i] == 'X':
        cntX += 1
    else:
        if cntX % 2 == 1: # X가 홀수개의 그룹이라면
            result = -1 # 폴리오미노로 덮을 수 없다.
            break
        else:
            cntA, r = divmod(cntX, 4)
            cntB = r //2
            result.append(polyA * cntA)
            result.append(polyB * cntB)
            result.append('.')
            cntX = 0

if result == -1:
    print(result)
else:
    result.pop() # 마지막에 추가했던 '.' 제거
    print(''.join(result))