import sys
input = sys.stdin.readline


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(node):
    traversal = []
    traversal.append(node.val)
    if node.left:
        traversal += preorder(tree[node.left])
    if node.right:
        traversal += preorder(tree[node.right])
    return traversal


def inorder(node):
    traversal = []
    if node.left:
        traversal += inorder(tree[node.left])
    traversal.append(node.val)
    if node.right:
        traversal += inorder(tree[node.right])
    return traversal


def postorder(node):
    traversal = []
    if node.left:
        traversal += postorder(tree[node.left])
    if node.right:
        traversal += postorder(tree[node.right])
    traversal.append(node.val)
    return traversal


n = int(input())  # 노드의 개수
tree = {}
for _ in range(n):
    v, l, r = input().split()
    if l == '.':
        l = None
    if r == '.':
        r = None
    tree[v] = Node(v, l, r)

print(*preorder(tree['A']), sep='')
print(*inorder(tree['A']), sep='')
print(*postorder(tree['A']), sep='')
