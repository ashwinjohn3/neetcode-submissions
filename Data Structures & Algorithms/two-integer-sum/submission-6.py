class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            target_diff = target - num
            if target_diff in num_map:
                return [num_map[target_diff], index]
            if not num_map.get(num):
                num_map[num] = index
        

