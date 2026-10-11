class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #store in a sorted list
        #example: [1,2,3,4,100,200]
        s_numbers = sorted(set(nums))

        longest = 0
        count = 0

        # go through each number in sorted list
        for i in range(len(s_numbers)):
            # skip first element and check if number is +1 than last element
            # example: [i,2,3,4,100,200] = skip
            # example: [1,i,3,4,100,200] = is 1+1 = i? yes
            if i > 0 and s_numbers[i] == s_numbers[i-1] + 1:
                # increment count
                count += 1
            else:
                # stop when sequence breaks
                count = 1
            
            #give which one was longest 
            #count can never be greater than 
            #longest, only temporarily
            longest = max(longest, count)

        return longest

