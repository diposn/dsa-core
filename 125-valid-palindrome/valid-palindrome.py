class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Two pointers      
        #example = racecar
        #left = 0 (r) 
        #right = 6 (r)
        left, right = 0, len(s) - 1
        
        #keep checking until both pointers meet
        #example
        # left = race
        # right = race
        # middle point 
        while left < right:

            #skip non aplhanumeric chars
            #example
            #skips any , : and keep nums and letter
            if not s[left].isalnum():
                left += 1
                continue

            #skip non aplhanumeric chars
            #example
            #skips any , : and keep nums and letter
            if not s[right].isalnum():
                right -= 1
                continue

            # comapre in lowercase
            if s[left].lower() != s[right].lower():
                # example
                # s = "hello"
                # h != O
                return False 

            #move pointers
            left += 1
            right -= 1
        
        return True
        