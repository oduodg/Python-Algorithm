from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 풀이 1. 가장 긴 동일 값의 경로
    result: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            print("dfs(", node, ")" )
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            print("left ", "dfs(", node.left, ")")
            right = dfs(node.right)
            print("right ", "dfs(", node.right, ")")

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            print('left: ',left, ' right:', right)
            self.result = max(self.result, left + right)
            print('self.result: ', self.result)
            # 자식 노드 상태값 중 큰 값 리턴
            print('리턴값: ', max(left,right))
            return max(left, right)

        dfs(root)
        return self.result

# 결과 확인
slt = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

#print(slt.longestUnivaluePath(root))

root1 = TreeNode(1)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(5)

print(slt.longestUnivaluePath(root1))