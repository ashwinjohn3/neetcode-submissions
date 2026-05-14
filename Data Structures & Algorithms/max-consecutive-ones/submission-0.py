class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = max_counter = nums[0]
        for i in range(1, len(nums)): 
            if nums[i] == 1:
                counter += 1
            else:
                max_counter = max(max_counter, counter)
                counter = 0
        return max(max_counter, counter)
            
        