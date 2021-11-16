import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 풀이 1. 개별 체이닝 방식을 이용한 해시 테이블 구현
    # 초기화
    def __init__(self):
        self.size = 1000  # 기본 사이즈는 1,000개 정도로 적당히 설정
        self.table = collections.defaultdict(
            ListNode)  # 각 ListNode를 담게 될 기본 자료형 선언

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size  # size의 개수만큼 모듈로 연산을 한 나머지를 해시값으로 정함
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:  # 이미 키가 존재할 경우
                p.value = value  # 값을 업데이트 함
                return
            if p.next is None:  # 다음 노드가 없으면
                break  # 아무것도 하지 않고 빠져나감
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# 결과 확인
hashMap = MyHashMap()
print(hashMap.put(1, 1))
print(hashMap.put(2, 2))
print(hashMap.get(1))
print(hashMap.get(3))
print(hashMap.put(2, 1))
print(hashMap.get(2))
print(hashMap.remove(2))
print(hashMap.get(2))
