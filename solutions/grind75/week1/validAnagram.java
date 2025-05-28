class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> counter = new HashMap<>();

        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0) - 1);
        }

        for (int val : counter.values()) {
            if (val != 0) return false;
        }

        return true;
    }
}