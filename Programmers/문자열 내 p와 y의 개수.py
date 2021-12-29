def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

# Test Case
s1 = "pPoooyY"
s2 = "Pyy"

print(solution(s1))
print(solution(s2))