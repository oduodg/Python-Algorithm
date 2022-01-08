import sys
input = sys.stdin.readline # 입력 가속

N = int(input()) # 온라인 저지 회원의 수

members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name]) # 나이를 숫자(int타입)로 입력받지 않으면 백준에서는 틀렸다고 나오므로 주의 

for age, name in sorted(members, key=lambda x:x[0]):
    print(age, name)
