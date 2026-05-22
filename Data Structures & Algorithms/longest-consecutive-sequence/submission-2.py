class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        longest = 1
        for i in range(len(nums)):
            num = nums[i]
            if num - 1 not in set_nums:
                length = 1
                while num + 1 in set_nums:
                    num = num + 1
                    length += 1
                longest = max(length, longest)
        return longest