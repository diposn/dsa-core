class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Ss = {}
        Ts = {}

        for char in s:
            Ss[char] = Ss.get(char, 0) + 1

        for char in t:
            Ts[char] = Ts.get(char, 0) + 1

        if Ss == Ts:
            return True
        else:
            return False
