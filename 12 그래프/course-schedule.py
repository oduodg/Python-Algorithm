from typing import List
import collections


class Solution:
    # 풀이 1. DFS로 순환 구조 판별
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()  # 방문한 노드를 담을 set 생성

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)  # i 노드 추가
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        return True

    # 풀이 2. 가지치기를 이용한 최적화
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()  # 추적 경로를 담을 set()
        visited = set()  # 방문한 노드를 담을 set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True


# 결과 확인
numCourses = 2
prerequisites = [[1, 0]]

numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]

numCourses3 = 3
prerequisites3 = [[0, 1], [1, 2], [2, 3]]

numCourses4 = 3
prerequisites4 = [[0, 1], [2, 3]]

numCourses5 = 3
prerequisites5 = [[0, 1], [0, 2], [1, 2]]

slt = Solution()
#print(slt.canFinish(numCourses, prerequisites))
#print(slt.canFinish(numCourses2, prerequisites2))
#print(slt.canFinish2(numCourses, prerequisites))
#print(slt.canFinish2(numCourses2, prerequisites2))
#print(slt.canFinish2(numCourses3, prerequisites3))
#print(slt.canFinish2(numCourses4, prerequisites4))
print(slt.canFinish2(numCourses5, prerequisites5))
