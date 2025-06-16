class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack


    """ 
    INTUITION (STACK)
        Initialize stack 
        Initialize mapping of parens, create a map of the pairs (closing to opening allows better code)

        Iterate through string
            If char is in the values (open parens), 
                Append current paren to stack
            Else if char in the keys, 
                if stack is empty or the paren at top of stack and expected are not same,
                    return false

        return if stack is empty or not
    """
