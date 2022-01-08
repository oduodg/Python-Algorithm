
import sys
input = sys.stdin.readline # 입력 가속
''' # 시간 초과
N = int(input()) # 좌표의 개수
nums = list(map(int, input().split()))
order = sorted(set(nums))
print(*[order.index(num) for num in nums]) # 인덱스에 접근하는 과정에서 시간초과가 나는 듯
'''

N = int(input())
nums = list(map(int, input().split()))
order = list(sorted(set(nums))) # 중복 제거
order = {order[i]: i for i in range(len(order))} # 딕셔너리로 만들어서 key, value를 갖게 함.
print(*[order[num] for num in nums]) # value 출력