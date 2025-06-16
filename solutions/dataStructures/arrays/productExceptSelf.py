class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n  # Initialize answer array with 1s

        cur = 1  # Prefix product
        for i in range(n):
            ans[i] *= cur
            cur *= nums[i]

        cur = 1  # Suffix product
        for i in range(n - 1, -1, -1):  # Fix: Correct reverse iteration
            ans[i] *= cur
            cur *= nums[i]

        return ans

    """
    INTUITION
    WE ARE TRYING TO CALCULATE THE PRODUCT OF ALL INDEXES EXCEPT CURRENT, THUS WE NEED THE PREFIX AND SUFFIX OF EACH INDEX
    WE WILL NEED TO USE A NEW ARRAY, CANNOT BE DONE INPLACE BECAUSE VALUES WOULD BE OVERWRITTEN
    GET PREFIX FIRST, THEN SUFFIX, AND RETURN

        Initialize an array with the same size but all values set to 1

        Cur variable to calculate our prefix index
        Loop through size of array, n
            Array[i] *= cur
            cur *= nums[i]

        Now we have to reverse iterate to get suffix index
        cur = 1
        Loop from n - 1 to -1,
            Array[i] *= cur
            cur *= Array[i]

        return Array
    """