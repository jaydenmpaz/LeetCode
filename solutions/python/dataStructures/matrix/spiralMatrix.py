class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        x, y = 0, 0
        dx, dy = 1, 0

        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "x"

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == "x":
                dx, dy = -dy, dx

            x += dx
            y += dy

        return res

    
    """
    Intuition
        We are tracing a spiral through a given matrix. We need to turn directions every time a boundary is met, so we are working towards the center



        Initialize variables for lengths of rows and cols
        Initialize variables for current position, x and y
        Initialize variables for tracking direction, dx and dy. Think of this as change in x and change in y

        We loop for rows * cols, because we want to visit each cell exactly once
            append the current coordinate to the res array
            mark current coordinate as visited with an "x"

            Now, our condition is checking if we go out of bounds or a cell is already visited
            0 <= x + ds < cols checks horizontally
            0 <= y + dy < rows checks vertically
            matrix[y + dy][x + dx] == "x" checks if visited
                change direction using formula dx, dy = -dy, dx if true

            increment x += dx
            increment y += dy

        
        return res
    """