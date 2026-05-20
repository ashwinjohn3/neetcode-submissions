class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_map = defaultdict(list)
        for str_ in strs:
            chara_list = [0]*26
            for char_ in str_:
                chara_list[ord(char_) - ord("a")] += 1
            tuple_map[tuple(chara_list)].append(str_)

        result = []
        for key in tuple_map.keys():
            result.append(tuple_map[key])
        return result

            
        