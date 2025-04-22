# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.inorder(root, results)
        return results

    def inorder(self, node: TreeNode, results: List[int]):
        if not node:
            return []
        self.inorder(node.left, results)
        results.append(node.val)
        self.inorder(node.right, results)

    """    
    Alternatively
        result = []

        def inorder(node):
            if not node:
                return []
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result
    """