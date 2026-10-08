class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {num : i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            need = target - num
            if need in values and values[need] != i:
                return [i, values[need]]