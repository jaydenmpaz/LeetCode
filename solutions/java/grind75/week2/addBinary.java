class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;

        // Iterate through each of the strings
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i) - '0';
            if (j >= 0) sum += b.charAt(j) - '0';

            sb.append(sum % 2); // Mod 2 tells us if current is 0 or 1
            carry = sum / 2;   // Carry calculated for next place

            i--;
            j--;
        }

        // Carry over for highest place
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }
}