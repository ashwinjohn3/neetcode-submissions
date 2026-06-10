class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(start_point):
            if start_point >= n:
                return start_point == n
            return dfs(start_point + 1) + dfs(start_point + 2)
        cache = [-1] * n 

        def dfs_with_cache(start_point):
            nonlocal cache
            if start_point >= n:
                return start_point == n 
            if cache[start_point] != -1:
                return cache[start_point]
            cache[start_point] = dfs_with_cache(start_point+1) + dfs_with_cache(start_point+2)
            return cache[start_point]
        return dfs_with_cache(0)
        