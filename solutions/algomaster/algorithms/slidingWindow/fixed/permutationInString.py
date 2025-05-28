class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:\
        # Initialize variables
        s1Freq, s2Freq = {}, {}
        s1Len, s2Len = len(s1), len(s2)

        if s1Len > s2Len:
            return False
        
        # Initialize Sliding Window
        for i in range(s1Len):
            s1Freq[s1[i]] = 1 + s1Freq.get(s1[i], 0)
            s2Freq[s2[i]] = 1 + s2Freq.get(s2[i], 0)

        # Check if initial is perm
        if (s1Freq == s2Freq):
            return True

        l = 0
        for r in range(s1Len, s2Len):
            s2Freq[s2[r]] = 1 + s2Freq.get(s2[r], 0)
            
            # Remove old character from the window
            s2Freq[s2[l]] -= 1
            if s2Freq[s2[l]] == 0:
                del s2Freq[s2[l]]  # Remove key if count is 0
            
            l += 1 # Increment left

            # Check if current window is a permutation
            if s1Freq == s2Freq:
                return True

        return False

    """
    FIXED SLIDING WINDOW
        Initialize dictionaries for frequencies
        Get variables for length

        Check if len of s1 > s2, cannot be permutation if longer

        Now, create the sliding window
        Iterate till length of s1
            add occuring characters and frequencies to dictionaries

        initial check to see if equal, return True. else continue.

        Now use 2 pointers, left and right to move the window along the input
            Subtract left element freq and add right to the window,
            if leftmost is now 0, pop it from dictionary

            increment the left

            now we check our 2 dictionaries for equality
                if true, we found a permutation
        
        by default if not found return false
    """