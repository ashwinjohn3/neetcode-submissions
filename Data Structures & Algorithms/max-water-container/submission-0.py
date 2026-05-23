class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = len(heights) - 1
        right_pointer = 0
        max_area = 0
        while left_pointer > right_pointer:
            width = left_pointer - right_pointer
            right_height = heights[right_pointer]
            left_height = heights[left_pointer]
            area = min(right_height, left_height)*width
            max_area = max(max_area, area)
            if right_height > left_height:
                left_pointer -= 1
            else:
                right_pointer += 1
        return max_area
        