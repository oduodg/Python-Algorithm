import sys
input = sys.stdin.readline # 입력 가속
n, k = map(int, input().split())
v = []
for i in range(n):
    coin = int(input())
    if coin <= k:
        v.append(coin)
cnt = 0
b = sys.maxsize
for i in range(-1,(len(v)+1)*(-1),-1): # 배열의 끝에서부터(큰 숫자부터)
    if k == 0:
        break
    if b < v[i]:
        continue
    a, b = divmod(k, v[i])
    cnt += a
    k = b

print(cnt)