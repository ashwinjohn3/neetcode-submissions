class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str_hash_map = {}
        for char_s in s:
            if char_s not in str_hash_map:
                str_hash_map[char_s] = 1
            else: 
                str_hash_map[char_s] += 1
        for char_t in t:
            if char_t not in str_hash_map:
                return False
            else:
                str_hash_map[char_t] -= 1
        for key in str_hash_map:
            if str_hash_map[key] == 0:
                pass
            else:
                return False
        return True

        