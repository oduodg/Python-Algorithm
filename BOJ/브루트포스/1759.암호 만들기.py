import sys
from itertools import combinations
input = sys.stdin.readline
l, c = map(int, input().split())
letters = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']
myVowels = [x for x in vowels if x in letters]

all = list(combinations(letters, l))

result = []
for password in all:
    consonants = list(set(password) - set(myVowels)) # 자음 개수
    # 모음이 1개 이상이고 자음이 2개 이상인 것들만
    if len(consonants) <= l-1 and len(consonants) >= 2:
        result.append(''.join(sorted(password)))

result.sort()

for password in result:
    print(password)