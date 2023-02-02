import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.left = None
        self.right = None
        self.x = x
        self.y = y

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    
    def insert(self, next_node):
        self.current_node = self.root
        while True:
            if next_node.x < self.current_node.x:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(next_node.value, next_node.x, next_node.y)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(next_node.value, next_node.x, next_node.y)
                    break
    
    def preorder(self):
        arr = []
        def _preorder(node):
            arr.append(node.value)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
        return arr
    
    def postorder(self):
        arr = []
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            arr.append(node.value)
        _postorder(self.root)
        return arr
                    
def solution(nodeinfo):    
    sorted_nodeinfo = sorted(nodeinfo, key=lambda x:(-x[1], x[0]))
    root_node = sorted_nodeinfo[0]
    root = Node(nodeinfo.index(root_node) + 1, root_node[0], root_node[1])
    bst = BinarySearchTree(root)
    
    for node in sorted_nodeinfo[1:]:
        bst.insert(Node(nodeinfo.index(node) + 1, node[0], node[1]))
    
    return [bst.preorder(), bst.postorder()]