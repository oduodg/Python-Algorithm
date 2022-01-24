def cantor(n):
    if n == 1:
        return '-'
    return cantor(n//3) + ' ' *(n//3) + cantor(n//3)

while True:
    try:
        n = int(input())
        print(cantor(3**n))
    except EOFError:
        break