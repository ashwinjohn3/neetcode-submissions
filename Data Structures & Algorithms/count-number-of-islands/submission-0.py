class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        islands = 0
        def dfs(point):
            r, c = point[0], point[1]
            if  not 0 <= r < lr or not 0 <= c < lc or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            dfs((r+1,c))
            dfs((r-1,c))
            dfs((r,c+1))
            dfs((r,c-1))
        

        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == "1":
                    dfs((i,j))
                    islands += 1
        return islands
            
        