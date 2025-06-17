# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two given trees are equal
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p and q:
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            return p is q

        # Traverse through the root of the tree and check if any subtree matches
        if not root:
            return False
        elif isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)