# 성공 코드
print(bin(int(input(), 8))[2:])

# 시간 초과 코드 -> C++로 하면 통과되는듯 하다..
n = list(input())
eight = ["000", "001", "010", "011", "100", "101", "110", "111"]
ans = ""

for i in range(len(n)):
	ans += eight[int(n[i])]

print(int(ans))