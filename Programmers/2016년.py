# 윤년: 4년에 한 번씩 2월이 29일까지 존재하는 연도

def solution(a, b):
    today = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    today = dict.fromkeys(today, 0)

    today = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11:30 }

    
    for i in range(1, a):
        b += today[i]

    day = b % 7

    if day == 0:
        return "THU"
    elif day == 1:
        return "FRI"
    elif day == 2:
        return "SAT"
    elif day == 3:
        return "SUN"
    elif day == 4:
        return "MON"
    elif day == 5:
        return "TUE"
    else:
        return "WED"
    


# Test Case
a = 5
b = 24
print(solution(a, b))