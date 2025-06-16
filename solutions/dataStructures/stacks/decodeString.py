class Solution:
    def decodeString(self, s: str) -> str:
        """
        When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
        push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
        the enclosed string k times.
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char =='[':
                # K (digit) has been parsed, save the current string a k to stack
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == "]":
                # Frame is completed, get the last current string and k from when
                # frame was opened and duplicate it
                last_string, last_k = stack.pop(-1)
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                # Read number place by place in decimal
                k = k * 10 + int(char)
            else:
                # Add char to our current string, building the frame
                current_string += char
            
        return current_string