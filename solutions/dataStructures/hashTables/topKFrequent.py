class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize dictionary to count freq and min_heap to process
        count = {}
        min_heap = []

        # Count occurrences
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Use min heap to get by priority of most occurring
        for key, val in count.items():
            heapq.heappush(min_heap, (-val, key)) # Use negative value to work for min heap

        # Initialize result array
        res = []

        # Pop the k most frequent elements and append to result
        while len(res) < k:
            res.append(heapq.heappop(min_heap)[1])

        return res
    