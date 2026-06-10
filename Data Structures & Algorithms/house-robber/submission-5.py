class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        cache = [-1] * length
        def dfs_with_cache(i):
            if i >= length:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(dfs_with_cache(i+1), nums[i] + dfs_with_cache(i+2))
            return cache[i]
        return dfs_with_cache(0)            