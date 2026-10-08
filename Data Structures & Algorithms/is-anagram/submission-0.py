

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for l in s:
            s_dict[l] = s_dict.get(l, 0) + 1
        for l in t:
            t_dict[l] = t_dict.get(l, 0) + 1
        return s_dict == t_dict