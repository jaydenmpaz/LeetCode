class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;

        int[][] directions = new int[][]{{0,1}, {0,-1}, {1,0}, {-1,0}};
        Deque<int[]> q = new ArrayDeque<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0 ) {
                    q.offer(new int[]{r, c});
                } else {
                    mat[r][c] = -1;  // Mark unvisited
                }
            }
        }

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int row = curr[0], col = curr[1];


            for (int[] direction : directions) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];

                // Check bounds and if unvisited
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && mat[newRow][newCol] == -1) {
                    mat[newRow][newCol] = mat[row][col] + 1;
                    q.offer(new int[]{newRow, newCol});
                }
            }
        }
        return mat;
    }
}