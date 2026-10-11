class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            #calc required number to reach target
            #example: [2,7,11] target = 9
            #example: 9 - num[i]
            #example: 9 - 2 = 7
            #example: 9 - 7 = 2
            comp = target - num

            # check if required num already in dict
            # example: comp = 7, not seen yet
            # example: comp = 2, yes [0,1]
            if comp in seen:
                return [seen[comp], i]
            
            #otherwise track the curr num
            seen[num] = i
        
        return []