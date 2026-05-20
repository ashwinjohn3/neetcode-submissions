class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        int_map = defaultdict(int)
        for i in nums:
            int_map[i] += 1
            if int_map[i] > 1:
                return True
        return False
            
        