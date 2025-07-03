class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting based on sort time allows us to easily compare with previous
        # intervals end time
        intervals = sorted(intervals, key=lambda x:x[0])
        merged = []
        

        # Iterate through the sorted intervals
        for interval in intervals:
            # If empty, or interval start time is after last intervals end,
            # Valid interval and add it to merged
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            # Else, we change the last intervals end time to the max of 
            # current or new interval's end
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged