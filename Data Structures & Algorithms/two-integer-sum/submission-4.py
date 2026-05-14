class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            diff_val = target - num
            if diff_val not in hash_map:
                hash_map[num] = index
            else: 
                return [hash_map[diff_val], index]
        