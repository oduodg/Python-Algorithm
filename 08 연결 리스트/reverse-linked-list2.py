class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이 1. 반복 구조로 노드 뒤집기
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외 처리
        if not head or m == n:
            return head

        start = ListNode(None)
        start.next = head
        # start, end 지정
        for _ in range(m-1):
            start = start.next
        end = start.next

    # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return start


# 결과 확인
m, n = 2, 4

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
result = slt.reverseBetween(head, m, n)
while result is not None:
    print(result.val)
    result = result.next
