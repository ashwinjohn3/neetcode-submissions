class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_map = defaultdict(list)
        for str_ in strs: 
            str_sorted = "".join(sorted(str_))
            print(str_sorted)
            sort_map[str_sorted].append(str_)
        
        result = []
        for key in sort_map.keys():
            print(key)
            result.append(sort_map[key])
        
        return result