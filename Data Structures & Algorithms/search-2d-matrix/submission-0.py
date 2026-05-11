class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mid = None
        low, high = 0, len(matrix)
        while low < high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                break
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid

        low, high = 0, len(matrix[mid])
        while low < high:
            midd = (low + high) // 2
            if matrix[mid][midd] == target:
                return True
            elif matrix[mid][midd] > target:
                high = midd
            else:
                low = midd + 1
        return False