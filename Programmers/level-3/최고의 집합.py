def solution(n, s):
    # 최고의 집합이 존재하지 않는 경우
    if n > s:
        return [-1]
    
    result = []
    
    for i in range(n, 0, -1):
        if i == 1:
            result.append(s)
            break
            
        num = s // i
        s -= num
        result.append(num)
        
    return sorted(result)