# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인 
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return

def solution(phone_book): # 효율성 테스트 3,4 시간초과 -> for문 이중중첩 시간복잡도 O(n^2)
    phone_book = sorted(phone_book, key=len)
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True

def solution2(phone_book): # while문 -> 효율성 테스트 통과
    phone_book.sort(reverse = True) # 사전식 역순으로 정렬
    idx = len(phone_book) - 1 
    while idx > 0: # 뒤에서부터 비교
        if phone_book[idx] == phone_book[idx-1][:len(phone_book[idx])]:
            return False
    return True

def solution3(phone_book): # startswith 사용
    phone_book.sort() # 사전순으로 정렬(11,1121,12,..) # 0을 a로 1을 b로 알파벳이라고 생각하면 편함
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True


# Test Case
TC1 = ["119", "97674223", "1195524421"]
TC2 = ["123","456","789"]
TC3 = ["12","123","1235","567","88"]

print(solution3(TC1)) # false
print(solution3(TC2)) # true
print(solution3(TC3)) # false