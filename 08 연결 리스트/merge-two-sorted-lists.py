from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 풀이1. 재귀 구조로 연결
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. l1이 None이면, l1과 l2를 무조건 바꾸어야 함
        # 2. 이 때, l2가 None 이면 바꾸면 안됨
        # 3. l1, l2 노드의 값이 작은 쪽이 l1이 됨
        if (not l1) or (l2 and (l1.val > l2.val)):  # 연산자 우선순위: > -> not -> and -> or
            l1, l2 = l2, l1

        # 이렇게 바꾸었을 때, l1이 None이면 l1, l2 둘다 None임
        # 둘다 None이라면 재귀를 더이상 하면 안되기에, if로 체크함
        # -> 아래의 if문이 실행되지 않으면 재귀 종료! l1 리턴
        if l1:
            # l1이 존재하면, l1의 next를 찾기 위한 재귀를 실행
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


# 결과 확인
if __name__ == "__main__":
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node3 = ListNode(4)
    l1_node1.next = l1_node2
    l1_node2.next = l1_node3
    l1 = l1_node1

    l2_node1 = ListNode(1)
    l2_node2 = ListNode(3)
    l2_node3 = ListNode(4)
    l2_node1.next = l2_node2
    l2_node2.next = l2_node3
    l2 = l2_node1

    slt = Solution()
    l1 = slt.mergeTwoLists(l1, l2)

    while l1 is not None:
        print(l1.val)
        l1 = l1.next
