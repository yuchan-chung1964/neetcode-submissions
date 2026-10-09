class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        top_k = sorted(counts, key=counts.get, reverse=True)[:k]
        return top_k