# 문제에서 깊이가 k인 완전 이진 트리는 총 2^k-1개의 노드로 이루어져 있다고 했으므로, 포화 이진 트리에 해당한다.
# 가장 가운데 수가 트리의 루트가 되고,
# 가운데를 기준으로 좌우로 나누면 왼쪽 서브트리, 오른쪽 서브트리로 나뉜다.
# 분할정복으로 가운데 수를 계속 찾고 좌우를 나누면서 진행한다.

k = int(input())
num = list(map(int, input().split()))
ans = [[] for _ in range(k)]  # 레벨에 따라 노드를 담을 리스트


def solution(tree, level=1):
    if level == k+1:
        return
    size = len(tree) // 2
    root = tree[size]
    ans[level-1].append(root)
    left_subtree = tree[:size]
    solution(left_subtree, level+1)
    right_subtree = tree[size+1:]
    solution(right_subtree, level+1)

    return ans


for nodes in solution(num):
    print(*nodes)
