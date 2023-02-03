def solution(n, build_frame):
    check = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]
    
    # 기둥 설치
    def install_gi(x, y):
        # 바닥 위
        if y == 0:
            return True
        # 보의 한쪽 끝 위
        if check[x-1][y][1] or check[x][y][1]:
            return True
        # 다른 기둥 위
        if check[x][y-1][0]:
            return True

        return False

    # 보 설치
    def install_bo(x, y):
        # 한쪽 끝이 기둥 위
        if check[x][y-1][0] or check[x+1][y-1][0]:
            return True
        # 양쪽 끝이 다른 보
        elif check[x-1][y][1] and check[x+1][y][1]:
            return True

        return False

    # 기둥 삭제
    def remove_gi(x, y):
        check[x][y][0] = False # 기둥 삭제
        # 위쪽 기둥 체크
        if check[x][y+1][0] and not install_gi(x, y+1):
            return False
        # 기둥 위쪽의 양 옆 보 체크
        if check[x-1][y+1][1] and not install_bo(x-1, y+1):
            return False
        if check[x][y+1][1] and not install_bo(x, y+1):
            return False

        return True

    # 보 삭제
    def remove_bo(x, y):
        check[x][y][1] = False # 보 삭제
        # 양 옆 보 체크
        if check[x-1][y][1] and not install_bo(x-1, y):
            return False
        if check[x+1][y][1] and not install_bo(x+1, y):
            return False
        # 왼쪽, 오른쪽 위에 있는 기둥 체크
        if check[x][y][0] and not install_gi(x, y):
            return False
        if check[x+1][y][0] and not install_gi(x+1, y):
            return False

        return True

    
    for x, y, a, b in build_frame:
        if a == 0: # 기둥
            if b == 0 and not remove_gi(x, y): # 삭제
                check[x][y][0] = True # 원상복귀
            elif b == 1 and install_gi(x, y): # 설치
                check[x][y][0] = True
        elif a == 1: # 보
            if b == 0 and not remove_bo(x, y): # 삭제
                check[x][y][1] = True # 원상복귀
            elif b == 1 and install_bo(x, y): # 설치
                check[x][y][1] = True
    
    result = []
    for i in range(n+1):
        for j in range(n+1):
            if check[i][j][0]:
                result.append([i, j, 0])
            if check[i][j][1]:
                result.append([i, j, 1])

    return result