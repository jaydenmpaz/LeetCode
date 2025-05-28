"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Empty base case
        if not node:
            return None

        # We will use a stack BFS to get all nodes
        start = node
        to_new = {}

        stack = [start]
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            to_new[node] = Node(val=node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        # Here, we will assign neighbors by indexing hashmap with old links
        for old, new in to_new.items():
            for neighbor in old.neighbors:
                new_neighbor = to_new[neighbor]
                new.neighbors.append(new_neighbor)

        # Return the copy of original input node in cloned graph
        return to_new[start]