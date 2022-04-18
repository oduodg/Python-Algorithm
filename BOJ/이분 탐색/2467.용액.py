import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

# 양끝값끼리 먼저 더하는게 빠름 -> 투포인터

i = 0
j = n-1

ans = sys.maxsize
while i < j:
    val = liquids[i] + liquids[j]
    if abs(val) < abs(ans):
        ans = val
        res = [liquids[i], liquids[j]]
        if ans == 0:
            break
    if  val > 0:
        j -= 1
    else: 
        i += 1

print(*res)