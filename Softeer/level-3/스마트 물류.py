import sys

n, k = map(int, input().split())
location = list(input())
check = [False for _ in range(n)]
dict = {} # 부품의 인덱스를 key로 갖는 dict
answer = 0

# 부품의 인덱스를 key로, value로 [] 빈 배열을 갖도록 초기화한다.
for i in range(n):
    if location[i] == 'H':
        dict[i] = []

# dict를 순회하면서
# 해당 부품을 집을 수 있는 거리만큼 순회한다.
# 인덱스가 올바른 범위 내에 있으며 로봇(P)이라면 
# dict[부품]에 로봇의 인덱스를 추가해준다.
for h in dict:
    for i in range(h-k, h+k+1):
        if 0 <= i < n and location[i] == 'P':
            dict[h].append(i)

# dict의 value(부품을 집을 수 있는 로봇의 인덱스들이 담긴 배열)의 길이로 정렬한다.
sorted_by_length = sorted(dict.items(), key=len)

# 빈 배열이면 건너뛴다.(집을 수 있는 로봇이 없다.)
# 배열의 길이가 1이면 집을 수 있는 로봇이 1개인 것이므로 
# 해당 로봇이 부품을 집지 않았다면 체크를 하고 answer을 1 증가시킨 후 continue
# 배열의 길이가 2 이상인 경우는 배열을 순회하면서 집을 수 있는 로봇이 있다면
# 체크를 하고 answer을 1 증가시킨다.
for v in sorted_by_length:
    if v[1] == []:
        continue
    if len(v[1]) == 1 and not check[v[1][0]]:
        check[v[1][0]] = True
        answer += 1
        continue
    
    for p in v[1]:
        if not check[p]:
            check[p] = True
            answer += 1
            break

print(answer)