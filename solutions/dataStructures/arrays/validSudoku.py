class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Keep a set of what has been seen in every row, column, and square
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # Iterate through all of the squares
        for r in range(9):
            for c in range(9):
                current = board[r][c]  # Current cell we are looking at
                
                # If empty, skip. No operation needed
                if current == ".":
                    continue

                # If the number in the current cell has already been seen in either
                # its current row, column, or square, return False
                if (current in rows[r] 
                    or current in cols[c]
                    or current in squares[(r // 3, c // 3)]):
                    return False

                # Otherwise, add the value to it's respective row, column, and square dictionary
                rows[r].add(current)
                cols[c].add(current)
                squares[r // 3, c // 3].add(current)

        return True