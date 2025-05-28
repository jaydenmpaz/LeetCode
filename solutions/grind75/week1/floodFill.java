class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        // Get the initial pixel's color
        int initial = image[sr][sc];

        // If the pixel is same, no changes needed according to example 2
        if (initial == newColor) return image;

        // Call fill helper function with stored initial and return result
        fill(image, sr, sc, initial, newColor);
        return image;
    }

    // Recursive function to DFS
    public void fill(int[][] image, int sr, int sc, int color, int newColor) {
        // First check within bounds, then check if color is same as original, if not end early.
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != color) return;
        
        // Set pixel to new color
        image[sr][sc] = newColor;

        // Recurse Up
        fill(image, sr - 1, sc, color, newColor);
        // Recurse Down
        fill(image, sr + 1, sc, color, newColor);
        // Recurse Left
        fill(image, sr, sc - 1, color, newColor);
        // Recurse Right
        fill(image, sr, sc + 1, color, newColor);
    }
}