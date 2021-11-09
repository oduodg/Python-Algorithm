from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이 1. 자료형 변환

    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 덧셈 결과를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
            int(''.join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 변환

        return self.toReversedLinkedList(str(resultStr))

    # 풀이 2. 전가산기 구현
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


# 결과 확인
slt = Solution()

nodeA_1 = ListNode(2)
nodeA_2 = ListNode(4)
nodeA_3 = ListNode(3)
l1 = nodeA_1
nodeA_1.next = nodeA_2
nodeA_2.next = nodeA_3

nodeB_1 = ListNode(5)
nodeB_2 = ListNode(6)
nodeB_3 = ListNode(4)
l2 = nodeB_1
nodeB_1.next = nodeB_2
nodeB_2.next = nodeB_3

result = slt.addTwoNumbers(l1, l2)
while result is not None:
    print(result.val)
    result = result.next

print()

nodeA_1 = ListNode(2)
nodeA_2 = ListNode(4)
nodeA_3 = ListNode(3)
l1 = nodeA_1
nodeA_1.next = nodeA_2
nodeA_2.next = nodeA_3

nodeB_1 = ListNode(5)
nodeB_2 = ListNode(6)
nodeB_3 = ListNode(4)
l2 = nodeB_1
nodeB_1.next = nodeB_2
nodeB_2.next = nodeB_3

result2 = slt.addTwoNumbers2(l1, l2)
while result2 is not None:
    print(result2.val)
    result2 = result2.next
