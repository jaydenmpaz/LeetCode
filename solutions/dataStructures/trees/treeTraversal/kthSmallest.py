# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.inorder(root, values)
        return values[k - 1]

    def inorder(self, node, values):
        if node is None:
                return
        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)

    # Intuition
    # Peform inorder traversal to get the items in the BST in ascending order
    # Grab the kth smallest element (remember it is 1 - indexed)