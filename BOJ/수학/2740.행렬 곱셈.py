import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrixA = []
for _ in range(n):
    matrixA.append(list(map(int, input().split())))

m, k = map(int, input().split())
matrixB = []
for _ in range(m):
    matrixB.append(list(map(int, input().split())))

ans = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        for l in range(k):
            ans[i][l] += matrixA[i][j] * matrixB[j][l]

for row in ans:
    for num in row:
        print(num, end=' ')
    print()
