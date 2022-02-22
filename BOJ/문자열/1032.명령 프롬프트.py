n = int(input())

files = []
for _ in range(n):
    files.append(list(input()))

for i in range(1, n):
    for j in range(len(files[0])):
        if files[0][j] != files[i][j]:
            files[0][j] = '?'

print(''.join(files[0]))
