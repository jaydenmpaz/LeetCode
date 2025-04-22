class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        count = {}

        for right, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
        
            res = max(res, right - left + 1)

        return res

    """
    Alternatively, use a set for presence approach
    def lengthOfLongestSubstring()
        left = max_length = 0
            char_set = set()
            
            for right in range(len(s)):
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1

                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
            
            return max_length    
    """
