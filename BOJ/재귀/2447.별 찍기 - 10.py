n = int(input())


def draw_star(n):
    if n == 3:
        return ['***', '* *', '***']

    Star = draw_star(n//3)
    L = []
    for star in Star:
        L.append(star*3)
    for star in Star:
        L.append(star + ' '*(n//3) + star)
    for star in Star:
        L.append(star*3)
    return L


print('\n'.join(draw_star(n)))
