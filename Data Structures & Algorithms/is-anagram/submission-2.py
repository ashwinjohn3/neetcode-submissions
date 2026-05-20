class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for chara in s:
            ana_map[chara] += 1
        for chara in t:
            ana_map[chara] -= 1
        for chara in ana_map.keys():
            if ana_map[chara] != 0:
                return False
        return True

        