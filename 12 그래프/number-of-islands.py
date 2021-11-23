from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):  # i는 행, j는 열
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            # 이미 탐색한 곳은 0으로 설정해 육지가 아닌 것으로 체크(다음에 다시 계산하는 경우 방지)
            grid[i][j] = 0
            # 동서남북 탐색
            dfs(i, j + 1)  # 동
            dfs(i, j - 1)  # 서
            dfs(i + 1, j)  # 남
            dfs(i - 1, j)  # 북

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # 육지를 발견하면
                    dfs(i, j)  # 탐색 시작
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1

        return count


# 결과 확인
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

slt = Solution()
print(slt.numIslands(grid))
print(slt.numIslands(grid2))
