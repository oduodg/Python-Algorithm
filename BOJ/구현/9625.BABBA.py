k = int(input())
screen = ['A']

while k > 0:
    for i in range(len(screen)):
        if screen[i] == 'A':
            screen[i] = 'B'
        else:
            screen[i] = 'BA'    
    screen = list(''.join(screen))
    k -= 1

screen = ''.join(screen)
print(screen.count('A'), screen.count('B'))