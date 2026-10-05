class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, num in enumerate(nums):
            #calc required number to reach target
            complement = target - num

            # check if required num already in dict
            if complement in seen:
                return [seen[complement], index]
            
            #otherwise track the curr num
            seen[num] = index
        
        return []