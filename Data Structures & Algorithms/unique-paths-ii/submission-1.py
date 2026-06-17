class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        lr = len(obstacleGrid)
        lc = len(obstacleGrid[0])

        matrix = [[0]*(lc+1)]*(lr+1)
        matrix[lr-1][lc-1] = 1

        for i in range(lr - 1, -1, -1): 
            for j in range(lc - 1, -1, -1):
                if obstacleGrid[i][j] != 1: 
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
                else:
                    matrix[i][j] = 0 

        return matrix[0][0]