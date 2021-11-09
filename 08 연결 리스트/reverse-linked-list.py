
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이 1. 재귀 구조로 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    # 풀이 2. 반복 구조로 뒤집기
    def reverseList2(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


# 결과 확인
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    slt = Solution()
    rev = slt.reverseList(head)

    print("재귀 결과")
    while rev is not None:
        print(rev.val)
        rev = rev.next

    print()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    rev = slt.reverseList2(head)

    print("반복 결과")
    while rev is not None:
        print(rev.val)
        rev = rev.next
