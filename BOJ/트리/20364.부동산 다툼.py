# 부모 노드의 번호는 자식 노드의 번호//2가 된다.
# 부모 노드가 점유되어 있으면 자식 노드를 점유할 수 없음.
# 타겟 노드부터 루트 노드까지 부모 노드를 찾아 거슬러 올라가면서 점유된 노드가 있다면 원하는 땅을 갖지 못함.
# 역순으로 거슬러 올라가므로 문제상으로 처음 만난 점유 노드의 땅 번호는 코드상으로 마지막으으로 만난 점유 노드의 땅 번호이다.

import sys
input = sys.stdin.readline
n, q = map(int, input().split())

visited = [False] * (n+1)  # True이면 점유된 땅, False이면 점유되지 않은 땅

for duck in range(q):
    land = int(input())
    target = land
    flag = 0  # flag의 값이 0이면 오리는 원하는 땅을 가질 수 있음.

    while target > 1:  # 루트 노드에 도달하기 전까지 반복
        if visited[target] == True:  # 점유된 땅을 밟으면
            flag = target  # flag에 점유된 땅 번호를 저장
        target = target//2  # 부모 노드로 올라감

    if flag:  # 원하는 땅을 가질 수 없는 오리는
        print(flag)  # 처음 만난 점유된 땅 번호를 출력한다.
    else:  # 원하는 땅을 가질 수 있는 오리는
        visited[land] = True  # 땅 점유 표시를 하고
        print(0)  # 0을 출력한다.
