import sys
input = sys.stdin.readline  # 입력 가속
n1, n2 = map(int, input().split())  # 각 그룹의 개미의 수
left = input().rstrip()  # 첫번째 그룹: 왼쪽에서 오른쪽으로 이동
right = input().rstrip()  # 두번째 그룹: 오른쪽에서 왼쪽으로 이동
t = int(input())  # t초
answer = left[::-1] + right  # 0초, 즉 두 그룹이 만났을 때
seq = list(answer)
cnt = 0  # 몇 초 지났는지 count
for i in range(n1+n2):
    if i < n1:
        seq[i] = [seq[i], 1]  # 1은 left 그룹의 개미
    else:
        seq[i] = [seq[i], -1]  # -1은 right 그룹의 개미
while answer != right + left[::-1]:  # 점프가 다 끝나기 전까지
    if cnt == t:
        break
    tmp = 0
    for i in range(len(seq)-1):
        if seq[i][1] == 1 and seq[i+1][1] == -1 and tmp != seq[i]:  # 한 번 점프한 개미는 거르기
            tmp = seq[i]
            seq[i] = seq[i+1]
            seq[i+1] = tmp
    cnt += 1
    answer = ''.join([ant for ant, dir in seq])
print(answer)
