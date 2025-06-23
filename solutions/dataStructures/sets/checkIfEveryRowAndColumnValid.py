class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for r in range(n):
            rowSeen = set()
            colSeen = set()
            for c in range(n):
                rowSeen.add(matrix[r][c])
                colSeen.add(matrix[c][r])

            if not (len(rowSeen) == len(matrix) and len(colSeen) == len(matrix)):
                return False

        return True