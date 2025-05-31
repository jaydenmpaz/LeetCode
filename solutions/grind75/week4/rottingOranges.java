class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int fresh = 0;

        // Initialize queue, add rotten position to queue or increment fresh count
        Queue<int[]> q = new LinkedList<>();
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    q.offer(new int[]{r, c});
                } else if (grid[r][c] == 1) {
                    fresh++;
                }
            }
        }

        // No fresh oranges to rot        
        if (fresh == 0) return 0;

        int minutes = 0;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // Do BFS on every initial rotten orange
        // Checks fresh count for optimized return if 0
        while (!q.isEmpty() && fresh > 0) {
            int size = q.size();
            boolean rottedThisMinute = false;

            for (int i = 0; i < size; i++) {
                int[] rot = q.poll();
                int row = rot[0], col = rot[1];

                for (int[] dir : directions) {
                    int newRow = row + dir[0];
                    int newCol = col + dir[1];

                    // If within bounds and element is fresh orange, change it
                    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && grid[newRow][newCol] == 1) {
                        grid[newRow][newCol] = 2;
                        q.offer(new int[]{newRow, newCol});
                        fresh--;
                        rottedThisMinute = true;
                    }
                }
            }
            if (rottedThisMinute) {
                minutes++;
            }
        }

        return fresh == 0 ? minutes : -1;
        }
}