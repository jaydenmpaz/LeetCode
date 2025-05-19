class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
         
        while left <= right:
            middle = (left + right) // 2

            # Target is found
            if nums[middle] == target:
                return middle

            # Check which half is sorted

            # Left of middle pointer is sorted
            elif nums[middle] >= nums[left]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
            # Right of middle pointer is sorted
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return - 1


        """
        Searches for a target value in a rotated sorted array using binary search.

        Intuition:
        In a rotated sorted array, one of the two halves (left or right) is always sorted.
        By identifying the sorted half at each step, we can determine whether the target
        lies within it:
        - If the target is in the sorted half, we discard the other half.
        - Otherwise, we search in the unsorted half.

        This allows us to maintain the O(log n) efficiency of binary search, even with the rotation.
        
        Args:
            nums (List[int]): Rotated sorted array.
            target (int): Value to search for.

        Returns:
            int: Index of target if found, else -1.
        """