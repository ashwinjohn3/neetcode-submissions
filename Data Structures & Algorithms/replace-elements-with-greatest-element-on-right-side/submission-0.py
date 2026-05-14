class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = 0
        while n+1 < len(arr):
            arr[n] = max(arr[n+1:])
            n += 1
        arr[len(arr) - 1] = -1
        print(arr)
        return arr
            
        