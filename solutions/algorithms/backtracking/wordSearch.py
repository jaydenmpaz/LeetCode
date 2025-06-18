class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == word[0] and self.searchWord(board, word, visited, 0, i, j)):
                    return True
            
        
        return False

    
    def searchWord(self, board, word, visited, index, i, j):
        # Word has been found
        if (index == len(word)):
            return True

        # Check within bounds, cell has already been visited (intersect), or if characters are not equal
        if (i < 0 or i >= len(board) or 
            j < 0 or j >= len(board[0]) or
            visited[i][j] or
            word[index] != board[i][j]):
            return False

        visited[i][j] = True

        # Explore all adjacent cells
        found = (
            self.searchWord(board, word, visited, index + 1, i + 1, j) or
            self.searchWord(board, word, visited, index + 1, i - 1, j) or
            self.searchWord(board, word, visited, index + 1, i, j + 1) or
            self.searchWord(board, word, visited, index + 1, i, j - 1)
        )

        # Backtrack
        visited[i][j] = False

        return found
