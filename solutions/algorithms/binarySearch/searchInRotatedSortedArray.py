class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        
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