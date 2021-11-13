class MyCircularQueue:
    # 풀이 1. 배열을 이용한 풀이
    def __init__(self, k: int):  # k는 큐의 크기
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0  # front의 포인터 p1
        self.p2 = 0  # rear의 포인터 p2

    # 요소 삽입 enQueue(): rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value  # rear 위치에 값을 넣는다.
            # 포인터를 한 칸 앞으로 이동한다. 단, 전체 길이만큼 나머지 연산을 하여 포인터의 위치가 전체 길이를 벗어나지 않게 한다.
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:  # rear 포인터 위치가 None이 아니라먄 다른 요소가 있는 공간이 꽉 찬 상태이거나 비정상적인 경우이므로 False 리턴
            return False

    # 요소 삭제 deQueue(): front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:  # front에 값이 있으면
            self.q[self.p1] = None  # None을 넣고
            self.p1 = (self.p1 + 1) % self.maxlen  # 포인터를 한 칸 앞으로 이동
            return True

    def Front(self) -> int:  # front에 값이 있으면 해당 값 리턴
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:  # rear 앞에 값이 있으면(enQueue()에서 rear에 값을 넣고 한 칸 앞으로 이동해서 값이 있는 부분은 rear가 가리키는 앞쪽이다. -> 그림으로 보면 이해 쉬움.) 해당 값 리턴
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
