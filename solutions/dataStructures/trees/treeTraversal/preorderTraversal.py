# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        self.preorder(root, results)
        return results

    def preorder(self, node: TreeNode, results: List[int]):
        if not node:
            return []
        results.append(node.val)
        self.preorder(node.left, results)
        self.preorder(node.right, results)

    """
    Alternatively 
        results = []

        def preorder(node):
            if not node:
                return []
            results.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return result
    """

    """
    INTUITION PRE ORDER TRAVERSAL

    Initialize result array

    Utilize a helper function to process our result
        if node is null:
            return []
        
        append the current node to global result var
        recursively call on node's left child
        recursively call on node's right child

    MAIN CALL TO HELPER FUNCTION WITH ROOT

    return result array
    """