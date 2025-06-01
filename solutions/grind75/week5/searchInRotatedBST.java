class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        // Modified binary search that leverages finding the sorted partition of the rotated array
        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Our target is found
            if (nums[mid] == target) {
                return mid;
            }

            // Left of middle pointer is sorted
            else if (nums[mid] >= nums[left]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Right of middle pointer is sorted 
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}