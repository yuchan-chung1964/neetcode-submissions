class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        sequences = {x:[x] for x in nums if x - 1 not in set_nums}
        for x in sequences.keys():
            curr = x
            while curr + 1 in set_nums:
                sequences[x].append(curr + 1)
                curr += 1
        return max((len(seq) for seq in sequences.values()), default=0)