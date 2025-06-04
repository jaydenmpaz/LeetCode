class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        The idea here is we are keeping track of 2 bounds. A high and a low.
        With these, if we find an element between the 2 bounds, we have found
        an increasing triplet.
        """
        first = float('inf')
        second = float('inf')

        for n in nums:
            if (n <= first):
                first = n
            elif (n <= second):
                second = n
            else:
                return True

        return False

    
