class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            distance = -(x*x + y*y)
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (distance, x, y))
            else:
                heapq.heappush(minHeap, (distance, x, y))
        
        return [(x, y) for (distance, x, y) in minHeap]