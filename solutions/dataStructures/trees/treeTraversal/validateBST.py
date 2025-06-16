# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            if not node:
                return True
            if not (node.val > minVal and node.val < maxVal):
                return False
            return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)

        return dfs(root, float('-inf'), float('inf'))
        
        # Intuition
        # Use dfs and check if each node is within the bounds of its children
        # Initial call on root with boundaries from -inf to inf