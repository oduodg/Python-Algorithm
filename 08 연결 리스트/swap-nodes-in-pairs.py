from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이 1. 값만 교환
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:  # cur is not None 으로 조건식을 하면 안되는 이유가 입력받은 노드의 개수가 홀수일 때 문제가 됨.
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # 풀이 2. 반복 구조로 스왑
    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next

        return root.next

    # 풀이 3. 재귀 구조로 스왑
    def swapPairs3(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs3(p.next)
            p.next = head
            return p
        return head

    # 풀이 4. 내 풀이(재귀)
    def swapPairs4(self, head: ListNode) -> ListNode:
        if head and head.next:  # head.next의 값도 있어야 pair로 스왑이 가능하다.
            p = head.next  # p는 head의 다음 값으로 지정
            head.next = p.next  # head는 p의 다음을 가리킴
            p.next = head  # p는 head를 가리킴

            head.next = self.swapPairs4(head.next)
            return p  # p가 제일 앞 노드에 위치해있으므로 p를 리턴
        return head  # 입력으로 홀수개의 노드가 들어왔을 때 head를 리턴해줘야 맨 뒤에 있는 노드까지 붙어서 나옴


# 결과 확인
print("풀이1")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

slt = Solution()
result = slt.swapPairs(head)
while result is not None:
    print(result.val)
    result = result.next

print("풀이2")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

result2 = slt.swapPairs2(head)
while result2 is not None:
    print(result2.val)
    result2 = result2.next

print("풀이3")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

result3 = slt.swapPairs3(head)
while result3 is not None:
    print(result3.val)
    result3 = result3.next

print("풀이4")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4

result4 = slt.swapPairs4(head)
while result4 is not None:
    print(result4.val)
    result4 = result4.next
