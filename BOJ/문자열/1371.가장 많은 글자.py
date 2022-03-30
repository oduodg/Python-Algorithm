import sys

s = sys.stdin.read()  # 입력을 한번에 다 받음
s = s.replace('\n', '').replace(' ', '')
counter = {}
for letter in s:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

max_value = max(list(counter.values()))

result = []
for key in counter.keys():
    if counter[key] == max_value:
        result.append(key)

result.sort()

for letter in result:
    print(letter, end='')
