class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if (nums[middle] > nums[middle + 1]):  # If middle is greater, peak is on left, so set right to middle
                right = middle
            elif (nums[middle] < nums[middle + 1]): # If middle is less, peak is on the right so set left to middle + 1
                left = middle + 1
            
        return left or right