def solution(s):
    s = sorted(s, reverse=True)
    s = ''.join(s)
    return s

# Test Case
s = "Zbcdefg"

print(solution(s))