from cgi import test
from typing import List
def maxProfit(self, prices: List[int]) -> int:
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result

# 결과 확인
test_case1 = [7,1,5,3,6,4]
print(maxProfit(test_case1))