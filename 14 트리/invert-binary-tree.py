from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 풀이 1. 파이썬다운 방식
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

    # 풀이 2. 반복 구조로 BFS
    def invertTree2(self, root:TreeNode) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)

        return root
    
    # 풀이 3. 반복 구조로 DFS
    def invertTree3(self, root:TreeNode) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root

    # 풀이 4. 반복 구조로 DFS 후위 순회
    def invertTree4(self, root:TreeNode) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left # 후위 순회

        return root


# 결과 확인

# level order
def levelorder(root):
    q = [root]
    while q:
        node = q.pop(0)
        print(node.val, '', end='')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

slt = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)


levelorder(slt.invertTree(root))

