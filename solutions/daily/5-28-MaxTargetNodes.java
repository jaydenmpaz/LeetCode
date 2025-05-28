class Solution {
    // Method to build adjacency list of input Trees
    private List<List<Integer>> buildList(int[][] edges) {
        int n = edges.length + 1;
        List<List<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        return adj;
    }

    // DFS Method to get the max amount of target nodes within k steps
    private int dfs(List<List<Integer>> adj, int u, int p, int k) {
        // Base case: Hops Exhausted
        if (k < 0) return 0;
        int cnt = 1;
        // Recurse on other nodes using (k-1) because we used a step
        for (int v : adj.get(u)) {
            if (v != p) cnt += dfs(adj, v, u, k - 1);
        }
        return cnt;
    }

    public int[] maxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        List<List<Integer>> adj1 = buildList(edges1);
        List<List<Integer>> adj2 = buildList(edges2);

        int n = adj1.size();
        int m = adj2.size(), maxB = 0;

        int[] res = new int[n];

        // Get the max amount of connections for the whole tree using (k-1) hops
        for (int i = 0; i < m; i++) {
            maxB = Math.max(maxB, dfs(adj2, i, -1, k - 1));
        }
        
        // For every node in Tree1, get the amount of targets + max from Tree2
        for (int i = 0; i < n; i++) {
            res[i] = dfs(adj1, i, -1, k) + maxB;
        }
        return res;
    }
}