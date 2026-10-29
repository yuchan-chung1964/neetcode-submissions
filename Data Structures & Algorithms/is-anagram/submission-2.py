class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for l in s:
            s_dict[l] += 1
        for l in t:
            t_dict[l] += 1
        return set(s_dict.items()) == set(t_dict.items())