class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        nonzero = 0
        length = len(nums)

        while i < length:
            if (nums[i] != 0):
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1
            i += 1
        return nums


    """
    INTUITION USE TWO POINTERS
    initialize nonzero, and i; nonzero will hold the index of the most current nonzero
    get length of input array

    while i < nums:
        if nums[i] != 0
            swap the 2, nums[i] nums[nonzero]
            increment nonzero
        increment i
    """