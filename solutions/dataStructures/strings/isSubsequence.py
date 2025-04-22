class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0, 0
        while (sp < len(s) and tp < len(t)):
            if (s[sp] == t[tp]):
                sp += 1
            tp += 1
        
        return sp == len(s)

    
    """
    Intuition (TWO POINTER)
        Initialize a pointer for each string, s and t

        Our conditions for looping are the lenghts of each pointer and their string's length respectively
        Ex: if sp > len(), we parsed through whole s string, same goes for t

            if the characters at the current pointer's places within the strings are equal,
                increment sp
            increment tp

            we only increment sp if they are equal because we are checking if s is a subsequence, meaning that orders of characters in s appearing in t matters.

        We return a boolean checking if our sp index is equal to the length of our string, meaning our string s is a subsequence of t
    """