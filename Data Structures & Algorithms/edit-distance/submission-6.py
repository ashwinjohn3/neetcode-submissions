class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        matrix = [[0]*(l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            matrix[i][l2] = l1 - i 
        for j in range(l2 + 1):
            matrix[l1][j] = l2 - j

        for i in range(l1 - 1, -1, -1): 
            for j in range(l2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    matrix[i][j] = matrix[i+1][j+1]
                else: 
                    matrix[i][j] = 1 + min(matrix[i+1][j+1], matrix[i+1][j], matrix[i][j+1])
        return matrix[0][0]
        