/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Global variable to store max diameter found so far
    private int result = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        // DFS Traversal from root, result will hold max diameter
        dfs(root);
        return result;
    }

    // Helper function to compute the depth of a node and update diameter variable result
    public int dfs(TreeNode curr) {
        // Base case: if current node is null, depth is 0
        if (curr == null) return 0;

        // Recursively compute the depth of left and right subtree
        int left = dfs(curr.left);
        int right = dfs(curr.right);

        // Diameter of node is left + right depth
        // This will update the global result if larger
        result = Math.max(result, left + right);

        // Return depth of current node to calculate diameter for rest
        return 1 + Math.max(left, right);
    }
}