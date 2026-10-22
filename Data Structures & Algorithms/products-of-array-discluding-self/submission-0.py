class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        products = []
        r_left = 1
        r_right = 1

        for i in range(len(nums)):
            left.append(r_left)
            right.append(r_right)
            r_left *= nums[i]
            r_right *= nums[-1 - i]
        
        for i in range(len(nums)):
            products.append(left[i] * right[-1 - i])
        
        return products