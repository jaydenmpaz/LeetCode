# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if not node:
                return False

            # Add current node to sum
            total += node.val
            
            # Leaf node is found
            if not node.left and not node.right:
                return total == targetSum

            # Not a leaf node, recurse on left and right and return true if either 
            # finds a path sum
            return dfs(node.left, total) or dfs(node.right, total)

        return dfs(root, 0)