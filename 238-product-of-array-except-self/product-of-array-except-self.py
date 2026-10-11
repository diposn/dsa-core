class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # create result array filled with 1
        result = [1] * len(nums)

        #calc products from left to right
        lp = 1
        for i in range(len(nums)):
            result[i] = lp
            lp *= nums[i]
        
        #calc products from right to left
        rp = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= rp
            rp *= nums[i]

        return result
