class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = self.get_product_without_zero(nums)
        result_arr = [product] * len(nums)
        zero_num = 0
        count_map = defaultdict(int)
        zero_index = -1

        for i, num in enumerate(nums):
            count_map[num] += 1
            if num == 0:
                zero_index = i
        
        if count_map[0] > 1:
            return [0]*len(result_arr)
        elif count_map[0] == 1:
            result_arr = [0] * len(nums)
            print(result_arr)
            print(zero_index)
            result_arr[zero_index] = product
        else:
            for i, product_ in enumerate(result_arr):
                result_arr[i] = product_//nums[i]
        
        return result_arr

    def get_product_without_zero(self,nums):
        product = 1
        for num in nums:
            if num == 0:
                continue
            product = product * num
        return product
                