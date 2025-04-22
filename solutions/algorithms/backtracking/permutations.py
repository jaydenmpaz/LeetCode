class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Base Case: there is only one item left to permute. Add single element to list
        if len(nums) == 1:
            return [nums[:]]

        # Initialize results array
        res = []

        # Iterate over each element in the nums
        for _ in range(len(nums)):

            # Pop element in front then call recursively on reduced list
            num = nums.pop(0)
            perms = self.permute(nums)

            # For each permutation generated, add previously popped value
            for p in perms:
                p.append(num)
            
            # Add all generated permutations to result array
            res.extend(perms)
            # Restore the original state for next iteration
            nums.append(num)

        return res

        """
        Intuition:
        We use recursion and backtracking to generate all permutations of the input list.
        At each recursive level, we pick an element (by popping from the front), generate
        all permutations of the remaining elements, and then append the picked element to each of those.
        After processing, we append the element back to restore the original list for the next iteration.
        This approach ensures we explore all possible orderings by rotating through each element
        in the list as the starting point in each recursive call.
        """