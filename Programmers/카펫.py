def solution(brown, yellow):
    total = brown + yellow
    for weight in range(total, 2, -1): # total에서 2까지 역순으로, 가로 >= 세로 이므로 weight를 기준으로 찾기
        if total % weight == 0:
            height = total // weight
        if yellow == (weight - 2) * (height - 2): # yellow 공식과 일치하는지 확인
            return [weight, height]

# Test Case
b1 = 10
y1 = 2

b2 = 8
y2 = 1

b3 = 24
y3 = 24

print(solution(b1, y1))
print(solution(b2, y2))
print(solution(b3, y3))