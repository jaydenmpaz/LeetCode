class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        int max = 0;

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            count.put(current, count.getOrDefault(current, 0) + 1);
            if (count.get(current) > count.getOrDefault(max, 0)) {
                max = current;
            }
        }
        return max;
    }
}