from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


# 결과 확인
slt = Solution()

lst1_1 = ListNode(1)
lst1_2 = ListNode(4)
lst1_3 = ListNode(5)
lst1_1.next = lst1_2
lst1_2.next = lst1_3
lst1 = lst1_1

lst2_1 = ListNode(1)
lst2_2 = ListNode(3)
lst2_3 = ListNode(4)
lst2_1.next = lst2_2
lst2_2.next = lst2_3
lst2 = lst2_1

lst3_1 = ListNode(2)
lst3_2 = ListNode(6)
lst3_1.next = lst3_2
lst3 = lst3_1

lists = [lst1, lst2, lst3]

result = slt.mergeKLists(lists)
while result is not None:
    print(result.val)
    result = result.next
