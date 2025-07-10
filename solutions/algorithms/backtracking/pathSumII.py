# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, path, total):
            # Node is null handling
            if not node:
                return

            # Add node to the path and increment sum so far
            path.append(node.val)
            total += node.val

            # Node is a leaf node, check if sum is equal
            if not node.left and not node.right:
                # Add path to result, need to copy over since recursion modify path variable
                if total == targetSum:
                    result.append(path[:])
            else:
                backtrack(node.left, path, total)
                backtrack(node.right, path, total)

            # We have finished exploring all paths containing the current node
            # Pop to remove current node from path and return to backtrack from
            # previous node on the call stack
            path.pop()

        result = []
        backtrack(root, [], 0)
        return result