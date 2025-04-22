class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_map = {}  # HashMap: num -> sequence length
        max_length = 0

        for num in nums:
            if num not in num_map:
                left = num_map.get(num - 1, 0)  # Length of left neighbor sequence
                right = num_map.get(num + 1, 0) # Length of right neighbor sequence
                current_length = 1 + left + right  # New sequence length

                # Store the sequence length for both ends
                num_map[num] = current_length
                num_map[num - left] = current_length
                num_map[num + right] = current_length

                max_length = max(max_length, current_length)

        return max_length

    """
    INTUITION WE WILL CALCULATE THE LEFT AND RIGHT NEIGHBORS SEQUENCE LENGTH OF EACH ELEMENT
        if nums empty
            return 0

        initialize a hashmap to count freqs
        intialize return value

        for num in nums:
            if num is not yet in nums
                calculate left, using default value of 0 if not found
                calculate right, using default value of 0 if not found
                the current length will now be 1 + left + right

                - Update the hash map at:
                - current number
                - left boundary: num - left
                - right boundary: num + right
            -This ensures we maintain correct lengths at the edges for future merges.
            - Update max_length if this sequence is the longest so far.

    Final result is the longest sequence found.
    """