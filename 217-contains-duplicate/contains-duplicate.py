class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        map = set()

        for num in nums:
            if num in map:
                return True
            else:
                map.add(num)
        return False