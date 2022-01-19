x = int(input()) # x번째
line = 1 # line은 대각선의 번호
while x > line: # x = 5, 4, 2
    x -= line # line = 1, 2, 3
    line += 1
if line % 2 == 0:
    a = x
    b = line +1 - x # a + b = line + 1
else:
    a = line +1 - x
    b = x

print(a, "/", b, sep = "")