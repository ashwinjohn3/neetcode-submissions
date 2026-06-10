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

        def dp_with_fib(n_steps):
            if n_steps <= 2:
                return n_steps
            dp = [0]*(n_steps+ 1)
            dp[1], dp[2] = 1, 2
            for i in range(3, n_steps + 1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n_steps]


        return dp_with_fib(n)
        