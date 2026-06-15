class Solution:
    def binary_search(self, row: List[int], target: int):
        l = 0
        r = len(row) 
        print(row)
        while l < r:
            mid = (l+r)//2
            if row[mid] < target:
                l = mid+1
            elif row[mid] > target:
                r = mid
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) 
        while top < bottom:
            mid = (top + bottom)//2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid 
            else:
                print(matrix[mid])
                return self.binary_search(matrix[mid], target)
                
        return False