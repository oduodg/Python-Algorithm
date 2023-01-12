def solution(clothes):
    dict = {}
    for name, kind in clothes:
        if kind in dict:
            dict[kind] += 1
        else:
            dict[kind] = 1
    
    result = 1
    for key, val in dict.items():
        result *= (val + 1) # +1은 착용하지 않는 경우 / 각각을 곱해주면 모든 경우의 수
    
    return result - 1 # 모두 안입는 경우 1 빼기
    


# Test Case
TC1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
TC2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(TC1))
print(solution(TC2))