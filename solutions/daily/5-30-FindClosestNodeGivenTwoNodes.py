class Solution:
    def dfs(self, node, edges, distance, visited):
        visited[node] = True
        neighbor = edges[node]
        if (neighbor != -1 and visited[neighbor] == False):
            distance[neighbor] = distance[node] + 1
            self.dfs(neighbor, edges, distance, visited)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        ans = -1
        minDistance = float('inf')
        node1Dist, visited1 = [0] * n, [False] * n
        node2Dist, visited2 = [0] * n, [False] * n

        self.dfs(node1, edges, node1Dist, visited1)
        self.dfs(node2, edges, node2Dist, visited2)

        for i in range(n):
            if (visited1[i] and visited2[i] and minDistance > max(node1Dist[i], node2Dist[i])):
                minDistance = max(node1Dist[i], node2Dist[i])
                ans = i

        return ans