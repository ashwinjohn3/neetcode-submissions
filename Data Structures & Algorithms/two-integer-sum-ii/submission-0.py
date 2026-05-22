class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        i = 0
        result = [] # add by +1
        while i < j: 
            diff = target - numbers[i]
            if diff > numbers[j]:
                i += 1
            elif diff < numbers[j]:
                j -= 1
            else:
                return [i+1, j+1]
        
        