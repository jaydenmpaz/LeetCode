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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root == null) return result;

        // Initialize a queue for BFS
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        // Will iterate till no further elements
        while (!q.isEmpty()) {
            // Create a list to store each level
            int size = q.size();
            List<Integer> current_level = new ArrayList<>();

            for (int i = 0; i < size; i++) {
                TreeNode current = q.remove();
                current_level.add(current.val);
                if (current.left != null) q.add(current.left);
                if (current.right != null) q.add(current.right);
            }
            result.add(current_level);
        }
        return result;
    }
}
