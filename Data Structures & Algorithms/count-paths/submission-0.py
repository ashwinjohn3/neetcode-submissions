class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0,1], [1,0]]
        matrix = [[0]*(n+1)]*(m+1)
        for i in range(m - 1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    matrix[i][j] += 1 
                else:
                    matrix[i][j] = matrix[i][j+1] + matrix[i+1][j]
        return matrix[0][0]

        