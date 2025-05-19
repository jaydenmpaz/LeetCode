class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Get the number of distinct elements in our array
        k = len(set(nums))

        # Initialize variables for left pointer, result, and counter hashmap
        left = 0
        res = 0
        counter = {}
        
        for i in range(len(nums)):
            # We are expanding the window to the right
            counter[nums[i]] = counter.get(nums[i], 0) + 1

            # Try to shrink from the left, while checking for k distinct elements
            while len(counter) == k:
                res += len(nums) - i
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
        
        return res

    # Intuition
    # Get the amount of disitinct elements, k
    # Initialize variables for sliding window apporach
    # Expand window all the way to the right, covering whole array
    # The idea is to shrink our window from the left while trying to keep same amount of distinct values