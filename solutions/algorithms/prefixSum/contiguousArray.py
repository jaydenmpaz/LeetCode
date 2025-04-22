class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        maxLength = 0
        mapping = {0 : 0}
        
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            elif num == 1:
                count += 1

            if count in mapping:
                maxLength = max(maxLength, index - mapping[count])
            else:
                mapping[count] = index
            
        return maxLength

    """
    Intuition:
    We want to find the longest contiguous subarray with an equal number of 0s and 1s.
    To do this efficiently, we treat 0 as -1 and 1 as +1. As we iterate through the array, we maintain a running `count` which represents the difference between the number of 1s and 0s seen so far.
    If at two different indices the count is the same, it means the number of 0s and 1s between those indices is equal. So, the length of the subarray between those two points is a candidate for the maximum.
    We use a dictionary (`mapping`) to remember the first index at which each count value appears. If we see the same count again, we calculate the distance between the current index and the stored index to get the subarray length.
    We update the maximum length whenever we find a longer valid subarray.
    This approach runs in linear time and space.
    """