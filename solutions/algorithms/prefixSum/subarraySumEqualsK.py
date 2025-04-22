class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subs = {0:1}
        running = 0
        res = 0

        for n in nums:
            running += n

            if running - k in subs:
                res += subs[running - k]

            subs[running] = 1 + subs.get(running, 0)

        return res

    """
    INTUITION: PREFIX SUM
    Initialize a dictionary to store the number of times a prefix sum has occured
    Start with 0 sum, for subarrays that start at index 0

    Initialize running sum and total subarray counter

    Iterate through array
        Add current item to total

        if total - k is in our dictionary, running sum is found:
            increment count with the amount of subarrays summing to k

        Record current prefix sum in dictionary, use default value or increment
    
    Return total subarray count
    """