a, b = map(int, input().strip().split(' '))
stars = '*' * a
for _ in range(b):
    print(stars)

# for문 사용하지 않고 풀기
# answer = ('*'*a + '\n')*b
# print(answer)