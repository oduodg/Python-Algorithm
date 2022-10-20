import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = list(map(int, input().split()))

def light_on_off(a, b, c):
	if a == 1:
		i, x = b, c
		s[i-1] = x
	else:
		l, r = b, c
		for j in range(l-1, r):
			if a == 2:
				s[j] = int(not s[j])
			elif a == 3:
				s[j] = 0
			else:
				s[j] = 1

for _ in range(m):
	a, b, c = map(int, input().split())
	light_on_off(a, b, c)

print(*s)