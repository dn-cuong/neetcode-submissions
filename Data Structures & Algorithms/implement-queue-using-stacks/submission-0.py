class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        temp = []
        while len(self.queue) > 1:
            temp.append(self.queue.pop())
        val = self.queue.pop()
        while temp:
            self.queue.append(temp.pop())
        return val

    def peek(self) -> int:
        temp = []
        val = None
        while len(self.queue) > 1:
            temp.append(self.queue.pop())
        val = self.queue.pop()
        self.queue.append(val)
        while temp:
            self.queue.append(temp.pop())
        return val

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()