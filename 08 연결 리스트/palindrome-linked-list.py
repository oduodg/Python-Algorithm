from typing import List, Deque
import collections


class ListNode:  # 연결 리스트 클래스 구현
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이 1. 리스트 변환
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []  # 리스트 변환

        # 입력으로 빈 값이 들어왔을 때, 예외처리
        if not head:
            return True

        node = head
        while node is not None:  # node가 존재하면(다음 값이 존재할 때 까지)
            q.append(node.val)  # q에 값을 추가
            node = node.next  # node는 다음 값을 가리킴

        while len(q) > 1:
            if q.pop(0) != q.pop():  # q의 첫번째 요소와 마지막 요소가 같지 않으면
                return False

        return True

    # 풀이 2. 데크를 이용한 최적화
    def isPalindrome2(self, head: ListNode) -> bool:
        # 데크 자료형 선언
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # 풀이 4. 런너를 이용한 우아한 풀이
    def isPalindrome3(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head  # slow와 fast 모두 head에서 시작
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # 입력값이 홀수일 때, slow 런너가 한 칸 더 앞으로 이동하여 중앙의 값을 빗겨 나가야 한다.(중앙에 위치한 값은 팰린드롬 체크에서 배제되어야 하기 때문)
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


# 결과 확인
if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    slt = Solution()
    print(slt.isPalindrome(head))
    print(slt.isPalindrome2(head))
    print(slt.isPalindrome3(head))

    nodeA = ListNode(1)
    nodeB = ListNode(2)
    head = nodeA
    nodeA.next = nodeB

    print(slt.isPalindrome(head))
    print(slt.isPalindrome2(head))
    print(slt.isPalindrome3(head))
