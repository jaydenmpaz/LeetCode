class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Base case for optimization
        if not intervals:
            return 0

        # We can use a greedy approach by comparing each intervals start time
        # to a prev tracked end time, we will keep track of valid intervals

        # Sort based on end times
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 1

        # For each interval, check if start is greater than our end, valid is
        # found
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        
        # Subtract total from amount of valid to get overlapping
        return len(intervals) - count