import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
	n = int(input())
	line = list(map(int, input().split()))
	#line.sort()
	#print(line[0], line[-1])
	print(min(line), max(line))