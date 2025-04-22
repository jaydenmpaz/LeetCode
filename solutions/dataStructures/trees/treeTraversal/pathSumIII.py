# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def dfs(node, current_sum):
            if not node:
                return
            current_sum += node.val
            if current_sum == targetSum:
                self.count += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        def traverse(node):
            if not node:
                return
            dfs(node, 0)  # Try all paths starting from this node
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.count