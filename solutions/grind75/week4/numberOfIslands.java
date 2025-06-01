class Solution {
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;

        // Call BFS on each cell that is part of an island
        for(int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    islands += 1;
                    BFS(grid, r, c, rows, cols);
                }
            }
        }
        return islands;
    }

    private void BFS(char[][] grid, int r, int c, int rows, int cols) {
        // Out of bounds check or if water is found, return to end
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == '0') return;

        // Set current pos to 0 the call on each adjacent cell
        grid[r][c] = '0';
        BFS(grid, r + 1, c, rows, cols);
        BFS(grid, r - 1, c, rows, cols);
        BFS(grid, r, c + 1, rows, cols);
        BFS(grid, r, c - 1, rows, cols);
    }
} 