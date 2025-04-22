class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) - 1

        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        
        return True

    
    """
    INTUITION 2 POINTER
    Use 2 pointers, 1 from left, and 1 from right to check each end of string till the converge in middle or different characters are found
        Convert string into single word and lowercase
        Initialize left and right pointer, 0 and last index respectively

        while left < right:
            check if character at left and right pointer are equal:
                return false if not
            increment left
            decrement right

        return true if is palindrome 
    """


    """
    Alternatively regex solution below
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1
    """