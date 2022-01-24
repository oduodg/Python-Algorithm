import sys, collections
input = sys.stdin.readline # 입력 가속

t = int(input()) # 테스트케이스의 수

for _ in range(t):
    n, m = map(int, input().split()) # 문서의 개수 n, 타겟 문서의 순서 m
    priority = list(map(int, input().split())) # n개 문서의 중요도
    cnt = 0 # 출력 순서
    idx = [i for i in range(n)] # 순서를 담을 인덱스 리스트
    doc = list(zip(priority, idx)) # (우선순위, 인덱스)
    doc = collections.deque(doc)  # 데크 타입으로
    target = (priority[m], m) # 타겟 문서
    while target in doc:
        if doc[0][0] == max(priority):
            doc.popleft()
            cnt += 1
            priority.remove(max(priority))
        else:
            doc.append(doc.popleft())
    print(cnt)