def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    else:
        if s.isdigit():
            return True
        else:
            return False

# Test case
TC1 = "a234"
TC2 = "1234"

print(solution(TC1))
print(solution(TC2))