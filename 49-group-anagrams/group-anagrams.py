class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    
        hashmap = {}

        for word in strs:

            key = "".join(sorted(word))

            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]

        return list(hashmap.values())