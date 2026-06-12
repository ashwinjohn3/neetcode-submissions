class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        max_area = 0
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(point):
            r, c = point[0], point[1]
            area = 0
            if not 0 <= r < lr or not 0 <= c < lc or grid[r][c] == 0:
                return 0
            # update the value to be 0 to mark it as visited
            grid[r][c] = 0
            area += 1
            for nr, nc in dirs:
                area += dfs((nr+r, nc+c))
            return area 

        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 1:
                    max_area = max(dfs([i,j]), max_area)
        return max_area