import sys
input = sys.stdin.readline

n = int(input()) # 용액의 수
liquids = sorted(list(map(int, input().split()))) # 오름차순 정렬

ans = sys.maxsize
result = []

for i in range(n-2):
    l = i+1 # 왼쪽 포인터: i 다음부터 오른쪽으로 진행
    r = n-1 # 오른쪽 포인터: 끝에서부터 왼쪽으로 진행
    while l < r:
        val = liquids[i] + liquids[l] + liquids[r]
        # 특성값이 0에 가장 가까운 값을 가진 세 용액으로 갱신
        if abs(val) <= abs(ans):
            ans = val
            result = [liquids[i], liquids[l], liquids[r]]
        
        if val == 0:
            print(*result)
            sys.exit()
        elif val < 0:
            l += 1
        else:
            r -= 1
print(*result)