class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def create_subset(i):
            # Base case: Considered all elements
            if i == len(nums):
                res.append(subsets[:]) # Add current subset to results
                return
            
            # Include nums[i] in current subset
            subsets.append(nums[i])
            # Recurse to next index with the element i included
            create_subset(i + 1)

            # Back track to remove the last added element, exclude i
            subsets.pop()
            # Recurse to next index without element i included
            create_subset(i + 1)

        # Build subsets from index 0
        create_subset(0)
        return res

    
    """
    Generates all possible subsets (the power set) of a given list of integers.

    This function uses backtracking to explore every combination of elements.
    At each step, it decides whether to include the current element or not,
    effectively building a binary tree of choices. When the end of the list is reached,
    the current subset is added to the result list.
    """