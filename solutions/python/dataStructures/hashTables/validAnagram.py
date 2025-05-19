class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}

        for x in s:
            counter[x] = counter.get(x, 0) + 1
        
        for x in t:
            if x not in counter or counter[x] == 0:
                return False
            counter[x] -= 1
        
        return True