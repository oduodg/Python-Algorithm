class MyQueue:
    # 풀이 1. 스택 2개 사용
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:  # input에 있는 값들을 output에 거꾸로 넣어줌
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []


# 결과 확인
queue = MyQueue()
queue.push(1)
print(queue.input)
queue.push(2)
print(queue.input)
print(queue.peek())
print(queue.pop())
print(queue.empty())
print(queue.pop())
print(queue.empty())
