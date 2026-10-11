class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        # create a map of set
        seen = set()

        # go through nums
        for num in nums:
            # if num in set
            if num in seen:
                # return dupicate
                return True
            # if num not in set add to set
            seen.add(num)
        # return false if no duplicate found
        return False