s = int(input())
n = 1
while True:
    if s <= (n * (n+1))//2:
        break
    n += 1

if s == (n * (n+1)) //2:
    print(n)
else:
    print(n-1)