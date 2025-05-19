# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        q = deque([root])

        while q:
            n = len(q)
            for i in range(n):
                # Remove from the front of the queue
                node = q.popleft()

                # Add the first node of this level (rightmost node in our traversal)
                if i == 0:
                    res.append(node.val)

                # Add the right child first, then left child, ensuring rightmost is processed first
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return res
