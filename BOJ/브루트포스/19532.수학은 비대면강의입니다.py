a, b, c, d, e, f = map(int, input().split())

# ax + by = c -> aex + bey = ce, adx + bdy = cd
# dx + ey = f -> bdx + bey = bf, adx + aey = af
# x = (ce-bf)/(ae-bd), y = (cd-af)/(bd-ae)

x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)
