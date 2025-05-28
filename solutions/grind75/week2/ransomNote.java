class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) return false;
        Map<Character, Integer> count = new HashMap<>();

        for (char c : magazine.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        for (char c : ransomNote.toCharArray()) {
            if (!count.containsKey(c) || count.get(c) < 1) return false;
            count.put(c, count.get(c) - 1);
        }
        return true;
    }
}