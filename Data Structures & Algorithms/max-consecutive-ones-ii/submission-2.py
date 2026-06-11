class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 1
        numZeroes = nums[left] == 0
        longest_sequence = 1 if len(nums) == 1 else 0
        lastZero_index = numZeroes
        while right < len(nums):
            if nums[right] == 0:
                if numZeroes + 1 > 1:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else: 
                    numZeroes += 1
            longest_sequence = max(longest_sequence, right - left + 1)
            right += 1
        return longest_sequence
        
            

