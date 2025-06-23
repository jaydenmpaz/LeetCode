class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        # while there is a carry to be processed
        while b != 0:
            carry = (a & b) << 1 # carry valye
            a = (a ^ b) # partial sum, no carry
            b = carry & mask
        
        # Handle negative values
        return a if a <= MAX_INT else ~(a ^ mask)
    
    # Essentially, the only way to do mathematic operations without the use 
    # of operators is bit manipulations.
    
    # We know that we can accomplish this by simply using every bit of b in a 
    # operation with the current value of a.
    
    # However, because we are working in python where ints can be much larger
    # than 32 bit, we need to consider a mask. This will help us only have to 
    # worry about values less than 32 bits and help with negative values as well.
    
    # The algorithm goes as follows,
    #     Two variables
    #     one for masking and holding the max positive integer possible with 32 bits

    #     WHILE there is a bit to be processed from b,
    #         calculate the carry value, XOR and bit shift
    #         calculate the partial sum
    #         set b to the carry value and mask it

    #     return what is left in a if it is LESS THAN max positive value of 32 bits
    #     else we need to mask it then negate.
    