'''
import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 사람의 수
bulk = []
for _ in range(n):
    x, y = map(int, input().split())
    bulk.append([x, y])

bulkArrange = sorted(bulk, key=lambda x: (-x[0], -x[1]))
count = [0] * n

for i in range(len(bulk)-1):
    cnt = 0
    for j in range(i+1, len(bulk)):
        if bulkArrange[i][0] > bulkArrange[j][0] and bulkArrange[i][1] > bulkArrange[j][1]:
            cnt += 1
        count[bulk.index(bulkArrange[i])] = cnt

answerDict = {ranks: 0 for ranks in count}
answerDict = dict(sorted(answerDict.items(), reverse=True))

countArrange = sorted(count, reverse=True)
rank = [0] * n
tmp = 1
for i in range(len(countArrange)):
    if i == 0:
        rank[i] = 1
    else:
        if countArrange[i-1] == countArrange[i]:
            rank[i] = rank[i-1]
            tmp += 1
        else:
            rank[i] = rank[i-1] + tmp
            tmp = 1

rank = list(set(rank))
i = 0
for key in answerDict.keys():
    answerDict[key] = rank[i]
    i += 1

answer = []
for i in range(len(count)):
    answer.append(answerDict[count[i]])
print(answer)
'''
import sys
input = sys.stdin.readline # 입력 가속

n = int(input()) # 사람의 수
people = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append([x, y])

for i in people:
    rank = 1
    for j in people:
        if (i[0] != j[0]) and (i[1] != j[1]): # 자기 자신은 비교에서 제외
            if (i[0] < j[0]) and (i[1] < j[1]): # j(다른 사람)가 x, y(몸무게, 키) 모두 큰 경우
                rank += 1
    print(rank, end=' ')