class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in values:
                return [values[need], i]   
            values[num] = i 
        return []