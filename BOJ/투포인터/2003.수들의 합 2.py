import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, 0
cnt = 0

sum = a[left]
while left < n and right < n:
    if sum < m:
        if left == n-1 or right == n-1:  # 끝에 도달했을 때 종료
            break
        right += 1
        sum += a[right]

    elif sum > m:
        if left == n-1:  # 끝에 도달했을 때 종료
            break
        left += 1
        right = left
        sum = a[left]

    else:
        cnt += 1
        if left == n-1:  # 끝에 도달했을 때 종료
            break
        left += 1
        right = left
        sum = a[left]

print(cnt)
