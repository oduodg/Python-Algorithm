import sys
input = sys.stdin.readline # 입력 가속

dwarfs = [0] * 9
for i in range(9):
    dwarfs[i] =  int(input())

remain = sum(dwarfs) - 100
for i in dwarfs:
    remain -= i
    if remain in dwarfs and dwarfs.index(remain) != dwarfs.index(i): # remain과 i가 같은 숫자인 경우를 인덱스 판별을 통해 제외해주어야 한다.
        dwarfs.remove(remain)
        dwarfs.remove(i)
        break
    else:
        remain += i

for height in sorted(dwarfs):
    print(height)