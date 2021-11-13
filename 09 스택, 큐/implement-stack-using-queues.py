import collections


class MyStack:
    # 풀이 1. push() 할 때 큐를 이용해 재정렬
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.pop())

    def pop(self) -> int:
        self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# 결과 확인
stack = MyStack()
stack.push(1)
print(stack.q)
stack.push(2)
print(stack.q)
stack.top()
print(stack.q)
stack.pop()
print(stack.q)
print(stack.empty())
