class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
            
        return False

    
    """
    INTUITION HASH MAP
        Initialize a hashmap to map the values to their last appearing index
        Loop through the nums array
        if val in seen, and it is within k indexes:
            return True, we have found a nearby duplicate
        else:
            set the mapping to most current index in seen
        
        return False
    """
