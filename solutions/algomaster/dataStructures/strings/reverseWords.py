class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words) 

    """
    STRING MANIPULATION
        SPLIT WORDS INTO ARRAY
        2 POINTER, ONE AT START ONE AT END
        
        WHILE LEFT < RIGHT (CONVERGING TO MIDDLE)
            SWAP THE ELEMENTS AT THE POINTERS
            INCREMENT LEFT
            DECREMENT RIGHT
        
        RETURN THE WORDS JOINED BACK AS A STRING
    """