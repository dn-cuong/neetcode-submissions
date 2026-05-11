from collections import deque
class MyStack:

    def __init__(self):
        self.dq = deque()
        self.dq2 = deque()
    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        for i in range(len(self.dq)-1):
            self.dq2.append(self.dq.popleft())
        x = self.dq.popleft()
        for i in range(len(self.dq2)):
            self.dq.append(self.dq2.popleft())
        return x

    def top(self) -> int:
        for i in range(len(self.dq)-1):
            self.dq2.append(self.dq.popleft())
        x = self.dq.popleft()
        for i in range(len(self.dq2)):
            self.dq.append(self.dq2.popleft())
        self.dq.append(x)
        return x

    def empty(self) -> bool:
        return len(self.dq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()