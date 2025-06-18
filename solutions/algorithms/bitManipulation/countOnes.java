class Solution {
    public int hammingWeight(int n) {\
        // Bit Shifting approach
        int ones = 0;
        while (n != 0) {
            ones += (n & 1);
            n >>>= 1;
        }
        return ones;
    }

    """
        Counting approach
        int ones = 0;
        while (n != 0) {
            ones += 1;
            n = n & (n-1);
        }

        return ones;
    """
}