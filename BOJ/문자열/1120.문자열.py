import sys

a, b = input().split()
la = list(a)
lb = list(b)

ans = sys.maxsize

for i in range(len(lb)-len(la)+1):
    cnt = 0
    for j in range(len(la)):
        if la[j] != lb[i+j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)
