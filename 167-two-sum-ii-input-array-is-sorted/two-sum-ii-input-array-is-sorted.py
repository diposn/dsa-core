class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        #[2,7,11,15]
        #example: l = 2, r = 15
        l, r = 0, len(numbers) - 1

        # l < r compares index 
        while l < r:
            
            # total = 2 + 15
            # total = 2 + 11
            # total = 2 + 7
            total = numbers[l] + numbers[r]

            # 2 + 15 != 9
            # 2 + 11 != 9
            # 2 + 7 == 8, TRUE, return [1,2]
            if total == target:
                return [l+1,r+1]

            # 2 + 15 > 9, TRUE
            #[2,7,11,15]
            #example: l=2, r=11

            # 2 + 11 > 9, TRUE
            #[2,7,11,15]
            #example: l=2, r=7
            elif total > target:
                r -= 1
            
            else:
                l += 1

        return []