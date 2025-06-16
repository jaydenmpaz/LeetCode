# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxAncestor):
            if not node:
                return 0

            if (node.val > maxAncestor):
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            elif (node.val == maxAncestor):
                return 1 + dfs(node.left, maxAncestor) + dfs(node.right, maxAncestor)
            else:
                return dfs(node.left, maxAncestor) + dfs(node.right, maxAncestor)
        
        return dfs(root, root.val)