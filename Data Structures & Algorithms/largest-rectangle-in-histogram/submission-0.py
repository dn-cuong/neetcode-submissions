class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for right in range(len(heights)):
            while stack and heights[right] < heights[stack[-1]]:
                index = stack.pop()
                height = heights[index]

                if stack:
                    width = right - stack[-1] - 1
                else:
                    width = right

                area = height * width
                max_area = max(max_area, area)

            stack.append(right)
        right = len(heights)

        while stack:
            index = stack.pop()
            height = heights[index]

            if stack:
                width = right - stack[-1] - 1
            else:
                width = right

            area = height * width
            max_area = max(max_area, area)

        return max_area