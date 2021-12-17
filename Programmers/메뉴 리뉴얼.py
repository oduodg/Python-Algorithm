import collections
import itertools

def solution(orders, course):
    result = []
    for i in course:
        temp = []
        for menu in orders:
            comb = itertools.combinations(sorted(menu), i) # sorted 할 것 ! (AB, BA는 동일한 구성)
            temp += comb
        counter = collections.Counter(temp)
        
        if len(counter) != 0 and max(counter.values()) > 1:
            mode = counter.most_common()[0][1] # 최빈값
        
        # most_common(1)은 최빈수가 같은 것이 여러개 존재해도 1개만 반환하므로
        for elem in counter.most_common():
            if elem[1] == mode:
                result.append(elem[0])

        # 문자열 합치기
        for i in range(len(result)):
            result[i] = ''.join(result[i])
    return sorted(result)

# Test Case
orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course1 = [2,3,4]
orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course2 = [2,3,5]
orders3 = ["XYZ", "XWY", "WXA"]
course3 = [2,3,4]

print(solution(orders1, course1))
print(solution(orders2, course2))
print(solution(orders3, course3))