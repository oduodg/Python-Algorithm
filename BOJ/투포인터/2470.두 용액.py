import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 전체 용액의 수
liquids = sorted(list(map(int, input().split())))

i, j = 0, len(liquids)-1
mixture = [liquids[i], liquids[j], abs(liquids[i] + liquids[j])]
value = []

while i < j:
    mixture = [liquids[i], liquids[j], abs(liquids[i] + liquids[j])]
    value.append(mixture)
    if liquids[i] + liquids[j] == 0:
        break
    elif liquids[i] + liquids[j] > 0:
        j -= 1
    else:
        i += 1

value.sort(key=lambda x: x[2])
print(value[0][0], value[0][1])