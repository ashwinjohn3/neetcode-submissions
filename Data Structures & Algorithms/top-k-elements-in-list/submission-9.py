class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        index_nested_arr = [[] for i in range(0, len(nums) + 1)]
        result_arr = []

        for num in nums:
            count_map[num] += 1
        
        for num, count in count_map.items():
            index_nested_arr[count].append(num)
        
        for i in range(len(nums), 0, -1):
            for num in index_nested_arr[i]:
                result_arr.append(num)
                if len(result_arr) == k:
                    return result_arr
        