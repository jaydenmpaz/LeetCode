class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int left = 0;
        Map<Character, Integer> counts = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);

            // If character has been seen and is within the current window
            if (counts.containsKey(c) && counts.get(c) >= left) {
                // Move the left pointer to the right of the last occurrence
                left = counts.get(c) + 1;
            }

            // Update the latest index of the character
            counts.put(c, right);

            // Update the result with the size of the current window
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}