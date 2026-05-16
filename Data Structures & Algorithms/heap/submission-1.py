class MinHeap:
    def __init__(self):
        self.heap = [None]

    def push(self, val: int) -> None:
        self.heap.append(val)
        if len(self.heap) <= 2:
            return 

        last = len(self.heap) - 1
        while last >= 1:
            parent = last // 2
            if parent != 0 and self.heap[parent] > self.heap[last]:
                self.heap[parent], self.heap[last] = self.heap[last], self.heap[parent]
                last = last // 2
            else:
                break
        

    def pop(self) -> int:
        if len(self.heap) < 2:
            return -1

        if len(self.heap) < 3:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        while i < len(self.heap) - 1:
            left = 2 * i 
            right = 2 * i + 1
            if left < len(self.heap) and right < len(self.heap):
                if self.heap[left] < self.heap[right] and self.heap[left] < self.heap[i]:
                    self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                    i *= 2
                elif self.heap[left] >= self.heap[right] and self.heap[right] < self.heap[i]:
                    self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                    i = i * 2 +1
                else:
                    break
            elif left >= len(self.heap) and right >= len(self.heap):
                break
            elif left >= len(self.heap):
                if self.heap[right] < self.heap[i]:
                    self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                    i = i * 2 +1
                else:
                    break
            elif right >= len(self.heap):
                if self.heap[left] < self.heap[i]:
                    self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                    i = i * 2
                else:
                    break
            else:
                break

        return res


    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [None] + nums[:]  # reset heap

        n = len(self.heap)

        def sift_down(i):
            while 2 * i < n:
                left = 2 * i
                right = 2 * i + 1
                smallest = i

                if left < n and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < n and self.heap[right] < self.heap[smallest]:
                    smallest = right

                if smallest == i:
                    break

                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest

        for i in range((n // 2), 0, -1):
            sift_down(i)