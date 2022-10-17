n = int(input())
l, r = 0, n
ans = 0
while l <= r:
	mid = (l + r) //2
	#print("mid=", mid)
	if mid**2 == n:
		ans = mid
		break
	elif mid**2 > n:
		r = mid - 1
		ans = mid
	else:
		l = mid + 1
	#print("ans=", ans)

print(ans)