class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)

        # Add all intervals which end before our new interval
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Check interval rollover/merging with new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # Insert out newInterval after potential merging steps
        merged.append(newInterval)

        # Insert the rest of the intervals, those that start after our new
        # interval's end time.
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged