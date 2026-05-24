class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_res = 0 
        l = 0
        maxf = 0 
        count_map = {}
        for r in range(len(s)):
            count_map[s[r]] = 1 + count_map.get(s[r], 0)
            maxf = max(maxf, count_map[s[r]])
            length = r - l + 1
            if length - max(count_map.values()) > k:
                count_map[s[l]] -= 1
                l += 1
            max_res = max(max_res, r - l + 1)
        return max_res
            
        