class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = -1 
        stack = []
        n = len(heights)
        for i in range(n):
            start = i 
            while stack and stack[-1][-1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i - index))
                start = index 
            stack.append((start, heights[i]))

        for i, h in stack: 
            maxArea = max((n - i)*h, maxArea)

        return maxArea
            