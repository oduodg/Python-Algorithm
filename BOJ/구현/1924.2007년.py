x, y = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] # 1월 ~ 11월 일 수
num = 0
if x == 1:
    num += y
else: 
    num = sum(month[:x-1]) + y

if num % 7 == 1:
    print("MON")
elif num % 7 == 2:
    print("TUE")
elif num % 7 == 3:
    print("WED")
elif num % 7 == 4:
    print("THU")
elif num % 7 == 5:
    print("FRI")
elif num % 7 == 6:
    print("SAT")
else:
    print("SUN")