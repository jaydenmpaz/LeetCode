class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case, not possible to have a substring if t longer than s
        if len(t) > len(s):
            return ""

        # Initialize the frequencies and counts of t
        t_count = defaultdict(int)
        for ch in t:
            t_count[ch] += 1
        
        # Initialize variables the length of t,
        # min_window will hold the indexes that our substring occur in the sliding window
        # start_index will be used to update min_window
        target_remaining = len(t)
        min_window = (0, float('inf'))
        start_index = 0

        # Expand Window
        # We will expand window to the size till character occurences of t are found in s
        for end_index, c in enumerate(s):
            # Current character exists in s
            if t_count[c] > 0:
                target_remaining -= 1
            t_count[c] -= 1

            # Contract Window
            # All target characters are in current silding window
            # We need to contract till we find the minimum
            if target_remaining == 0:
                while True:
                    # Case where the first letter in s is needed for substring
                    c_at_start = s[start_index]
                    if t_count[c_at_start] == 0:
                        break

                    # Increment count of current character and iterate start_index to shrink the window
                    t_count[c_at_start] += 1
                    start_index += 1

                # Update minimum window check
                if end_index - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)

                # Add back for validitiy of removing character
                t_count[s[start_index]] += 1
                target_remaining += 1
                start_index += 1
        
        return "" if min_window[1] > len(s) else s[min_window[0] : min_window[1] + 1]