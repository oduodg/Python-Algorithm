def solution(n):
    watermelon = "수박"
    if n % 2 == 0:
        return watermelon * (n//2)
    else:
        return watermelon * (n//2) + "수"


# Test Case
print(solution(3))
print(solution(4))
