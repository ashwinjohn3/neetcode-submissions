class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        for i in range(len(t)):
            if t[i] not in count: 
                return False
            else:
                count[t[i]] -= 1
        
        for k, v in count.items():
            if v != 0:
                return False
        return True