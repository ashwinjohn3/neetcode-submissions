class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = numRows
        tri = [[1]]
        for i in range(1, l):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = tri[i-1][j-1] + tri[i-1][j]
            tri.append(row)
        return tri
    

        
        