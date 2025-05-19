class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Binary search helper, with extra parameter to indicate left or right
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
                
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1  # Check further left indexes
                    else:
                        left = mid + 1  # Check further right indexes
                
            return idx
        
        # Get the search range by calling twice, to find both bounds
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]