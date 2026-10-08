class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i, s in enumerate(strs):
            chars = tuple(sorted(s))
            if chars in anagrams:
                anagrams[chars].append(s)
            else:
                anagrams[chars] = [s]
        return list(anagrams.values())