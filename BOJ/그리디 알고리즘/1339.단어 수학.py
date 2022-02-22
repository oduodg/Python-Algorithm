import sys
input = sys.stdin.readline  # 입력 가속
n = int(input())
dic = {}
for _ in range(n):
    word = input()
    for i in range(len(word)-1):  # 맨 뒤 공백 때문에 -1
        if word[i] in dic:
            dic[word[i]] += 10**(len(word)-2-i)
        else:
            dic[word[i]] = 10**(len(word)-2-i)

dic = sorted(dic.items(), key=lambda x: -x[1])
num = 9
total = 0
for i in range(len(dic)):
    total += dic[i][1] * num
    num -= 1

print(total)
