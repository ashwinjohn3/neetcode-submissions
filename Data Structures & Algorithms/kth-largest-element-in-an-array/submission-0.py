class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        reverse_nums = [-num for num in nums]
        heapq.heapify(reverse_nums)
        for i in range(k - 1):
            heapq.heappop(reverse_nums)
        return -1*heapq.heappop(reverse_nums)
        