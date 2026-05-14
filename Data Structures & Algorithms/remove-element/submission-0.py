class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - 1
        while n >= 0:
            if (nums[n] == val): 
                nums.pop(n)
            n -= 1
        print(nums)
        return len(nums)
