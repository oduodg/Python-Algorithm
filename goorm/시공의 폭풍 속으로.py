'''
# 문제 ⭐️1 - 구현
시공의 폭풍은 87명의 영웅(편의상 1~87번까지 번호가 매겨져 있다고 하자)들 중 각 팀별로 5명씩 골라 총 10명이 플레이하는 게임이다. 당신의 팀원들이 선택한 4명의 영웅들과 당신이 선택하길 원하는 영웅 5명의 번호가 주어졌을 때, 선택할 수 있는 영웅이 몇 명인지 세어보자!
# 입력
첫 번째 줄에는 당신의 팀원들이 선택한 4명의 영웅 번호가 중복 없이 공백으로 구분되어 주어진다. 두 번째 줄에는 당신이 선택하고자 하는 5명의 영웅 번호가 중복 없이 공백으로 구분되어 주어진다.
# 출력
당신이 선택하고자 하는 영웅들 중 선택할 수 있는, 즉 이미 팀원이 선택한 영웅이 아닌 영웅의 수를 출력한다.
'''
# try 1 - success O(n^2) 브루트포스
'''
import sys
input = sys.stdin.readline # 입력 가속
myTeam = list(map(int, input().split()))
myHero =  list(map(int, input().split()))

ans = 0
for i in myTeam:
	for j in myHero:
		if i == j:
			ans += 1
			break
print(5-ans)
'''
# try 2 - success O(n) 체크 배열
import sys
input = sys.stdin.readline # 입력 가속
chk = [0] * 88 # 선택하지 않은 영웅은 0으로 표기
ans = 0
myTeam = list(map(int, input().split()))
for i in myTeam:
	chk[i] = 1 # 선택한 영웅은 1로 표기

myHero = list(map(int, input().split()))
for j in myHero:
	if chk[j] == 0:
		ans += 1

print(ans)

# TC 1
'''
input
1 5 7 10
1 2 3 4 5
output
3
'''
# TC 2
'''
input
1 2 3 4
1 2 3 4 5
output
1
'''