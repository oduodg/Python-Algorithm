def solution(numbers, hand):
    answer = []
    
    leftThumb = 10 # 왼손 엄지손가락 시작 위치(*)
    rightThumb = 12 # 오른손 엄지손가락 시작 위치(#)

    for number in numbers:
        # 좌측 배열 = 왼손 엄지손가락이 입력
        if number == 1 or number == 4 or number == 7:
            answer.append('L')
            leftThumb = number
        # 우측 배열 = 오른손 엄지손가락이 입력
        elif number == 3 or number == 6 or number == 9:
            answer.append('R')
            rightThumb = number
        # 중간 배열
        else:
            # number가 0인 경우 11로 변경시켜줌
            if number == 0:
                number = 11
            
            # 왼손 엄지손가락과의 거리 측정
            if leftThumb == number:
                leftDistance = 0
            else:
                leftDistance = abs(leftThumb-number) // 3 + abs(leftThumb-number) % 3
            # 오른손 엄지손가락과의 거리 측정  
            if rightThumb == number:
                rightDistance = 0
            else:
                rightDistance = abs(rightThumb-number) // 3 + abs(rightThumb-number) % 3

            # 거리 비교            
            if leftDistance == rightDistance:
                if hand == 'left':
                    answer.append('L')
                    leftThumb = number
                else:
                    answer.append('R')
                    rightThumb = number
            elif leftDistance < rightDistance:
                answer.append('L')
                leftThumb = number
            else:
                answer.append('R')
                rightThumb = number          
        
    return ''.join(answer)

# Test Case
TC1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
TC2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
TC3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(solution(TC1, 'right'))
print(solution(TC2, 'left'))
print(solution(TC3, 'right'))