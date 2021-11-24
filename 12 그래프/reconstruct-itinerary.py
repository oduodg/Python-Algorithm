from typing import List
import collections


class Solution:
    # 풀이 1. DFS로 일정 그래프 구성
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)  # "from"을 key로, "to"를 value list로

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))  # value list의 가장 앞에 있는 원소를 추출
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

    # 풀이 2. 스택 연산으로 큐 연산 최적화 시도
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        route = []

        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

        # tickets3의 경우
        # dfs(JFK), <dfs(KUL), route = [KUL]>, \
        # <dfs(NRT), <dfs(JFK) , route = [KUL, JFK]>, route = [KUL, JFK, NRT]> \
        # route = [KUL, JFK, NRT, JFK]>
        # 거꾸로 -> route = [JFK, NRT, JFK, KUL]

    # 풀이 3. 일정 그래프 반복

    def findItinerary3(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

# graph = {'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}, stack = ['JFK']
# graph = {'ATL': ['JFK', 'SFO'], 'JFK': ['SFO'], 'SFO': ['ATL']}, stack = ['JFK','ATL']
# graph = {'ATL': ['SFO'], 'JFK': ['SFO'], 'SFO': ['ATL']}, stack = ['JFK','ATL','JFK']
# graph = {'ATL': ['SFO'], 'JFK': [], 'SFO': ['ATL']}, stack = ['JFK','ATL','JFK','SFO']
# graph = {'ATL': ['SFO'], 'JFK': [], 'SFO': []}, stack = ['JFK','ATL','JFK','SFO','ATL']
# graph = {'ATL': [], 'JFK': [], 'SFO': []}, stack = ['JFK','ATL','JFK','SFO','ATL','SFO']


# 결과 확인
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]

slt = Solution()
print(slt.findItinerary(tickets))
print(slt.findItinerary2(tickets))
print(slt.findItinerary3(tickets))
print(slt.findItinerary(tickets2))
print(slt.findItinerary2(tickets2))
print(slt.findItinerary3(tickets2))
print(slt.findItinerary(tickets3))
print(slt.findItinerary2(tickets3))
print(slt.findItinerary3(tickets3))
