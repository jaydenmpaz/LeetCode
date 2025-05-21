class Solution {
    public int binarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int middle = (left + right) / 2;
            int current_value = nums[middle];
            
            if (current_value < target) {
                left = middle + 1;
            }
            else if (current_value > target) {
                right = middle - 1;
            }
            else {
                return middle;
            }
        }
        return -1;
    }
}