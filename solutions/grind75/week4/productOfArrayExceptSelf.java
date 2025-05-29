class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Two pass, prefix & suffix product calculation, then times by current element
        int[] answer = new int[nums.length];
        Arrays.fill(answer, 1);

        // Generate prefix product
        int curr = 1;
        for (int i = 0; i < nums.length; i++) {
            answer[i] *= curr;
            curr *= nums[i];
        }

        // Generate suffix product
        curr = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= curr;
            curr *= nums[i];
        }

        return answer;
    }
}