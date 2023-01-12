import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 리스트를 힙으로 변환

    cnt = 0

    while scoville[0] < K:
        newK = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, newK)
        cnt += 1

        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return cnt

# Test Case
scoville1 = [1,2,3,9,10,12]
K1 = 7

print(solution(scoville1, K1))
