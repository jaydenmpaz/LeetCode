class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if (nums[middle] > nums[right]):
                left = middle + 1
            else:
                right = middle
        
        return nums[left]

        """ 
        INTUITION: BINARY SEARCH
        INITIALIZE VARIABLES FOR LEFT AND RIGHT POINTERS

        WHILE L < R:
            CALCULATE MIDDLE
            CHECK IF MIDDLE IS LARGER THAN RIGHT,
            IF IT IS THEN WE WANT TO SEARCH THE RIGHT (SET LEFT TO MIDDLE + 1)
            ELSE
            SEARCH THE LEFT (SET THE RIGHT TO MIDDLE)

        RETURN NUMS[LEFT]
        """