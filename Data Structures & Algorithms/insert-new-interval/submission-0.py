class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        newStart, newEnd = newInterval

        for start, end in intervals:

            if end < newStart:
                result.append([start, end])

            elif start > newEnd:
                result.append([newStart, newEnd])
                newStart, newEnd = start, end

            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)

        result.append([newStart, newEnd])

        return result