class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        slen = len(s) 
        tlen = len(t)
        while i < slen and j < tlen:
            if s[i] == t[j]:
                print(f"MATCHED: {s[i]} == {t[j]}")
                i += 1
            j += 1
        return i == slen 
            

        