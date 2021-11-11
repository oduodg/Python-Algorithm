class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이 1. 반복 구조로 홀짝 노드 처리
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외 처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head


# 결과 확인
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
result = slt.oddEvenList(head)

while result is not None:
    print(result.val)
    result = result.next
