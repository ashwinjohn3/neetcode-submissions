class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)
        for c in s: 
            counter[c] += 1 
        for k in t: 
            counter[k] -= 1 
        
        for k, v in counter.items():
            if v != 0:
                return False
        return True