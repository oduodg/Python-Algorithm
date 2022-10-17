'''
# 문제 ⭐️1 - 구현
고대 유적지를 연구하던 인디아나 홍스는 유적지의 벽에 새겨진 엄청난 숫자들을 발견했다. 벽에 새겨진 숫자 중 일부는 비밀스러운 정보를 조회할 수 있는 열쇠 역할을 하는 비밀스러운 수이다. 오랜 연구 끝에 인디아나 홍스는 엄청난 숫자들이 특별한 규칙을 가지고 있다는 사실을 발견하였다. 엄청난 숫자들 중 의미 있는 숫자들은 항상 2^k(0<=k) 형태로 적혀 있고, 그 외의 수들은 모두 비밀스러운 정보와는 관련 없다는 것이다.

인디아나 홍스를 도와 벽에 새겨진 숫자가 비밀스러운 정보인지 아닌지를 판별해보자!

# 입력
첫 번째 줄에 벽에 새겨진 수가 주어진다. 이 수는 10^18 이하의 자연수이다.

# 출력
주어진 수가 비밀스러운 정보를 가진 숫자라면 Yes, 아니라면 No를 출력한다.
'''

# 2의 제곱수이면 Yes, 아니면 No를 출력
import sys
input = sys.stdin.readline # 입력 가속
n = int(input())
flag = True
while n >= 1:
	if n == 1 or n == 2:
		break
	if n % 2: # n이 홀수일 때
		flag = False
		break
	else: # n이 짝수일 때
		n = n//2

if flag:
	print("Yes")
else:
	print("No")

# TC 1
'''
input
32
output
Yes
'''
# TC 2
'''
input
1
output
Yes
'''
# TC 3
'''
input
10
output
No
'''