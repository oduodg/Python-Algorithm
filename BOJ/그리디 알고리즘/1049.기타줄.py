import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 기타줄의 개수 n, 기타줄 브랜드의 개수 m
package = 1001
piece = 1001
for _ in range(m):
    a, b = map(int, input().split())
    package = min(package, a)
    piece = min(piece, b)

c, d = divmod(n, 6)
print(min(c * package, 6 * c * piece) + min(d * piece, package))
