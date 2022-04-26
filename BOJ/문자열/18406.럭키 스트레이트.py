n = int(input())
l = list(str(n))
left = 0
right = 0
for i in range(len(l)):
    if i < len(l)//2:
        left += int(l[i])
    else:
        right += int(l[i])

if left == right:
    print("LUCKY")
else:
    print("READY")