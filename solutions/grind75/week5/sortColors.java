class Solution {
    public void sortColors(int[] nums) {
        HashMap<Integer, Integer> mapping = new HashMap<>();

        for (int n : nums) {
            mapping.put(n, mapping.getOrDefault(n, 0) + 1);
        }

        int id = 0;
        for (int i = 0; i < 3; i++) {
            int freq = mapping.getOrDefault(i, 0);
            Arrays.fill(nums, id, id + freq, i);
            id += freq;
        }
    }
}