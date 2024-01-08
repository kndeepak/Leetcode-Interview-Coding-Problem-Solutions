class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        rows, cols = len(board), len(board[0])
        # Initialize a set to keep track of the visited cells
        path = set()

        # Define the DFS function
        def dfs(r, c, i):
            # If the entire word is found, return True
            if i == len(word):
                return True

            # Check for out-of-bounds, character mismatch, or already visited cell
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            # Add the current cell to the visited path
            path.add((r, c))

            # Recursively search in all four directions
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            # Remove the current cell from the visited path
            path.remove((r, c))

            return res

        # Iterate through each cell of the board
        for r in range(rows):
            for c in range(cols):
                # Start DFS from each cell
                if dfs(r, c, 0):
                    return True  # Return True if the word is found

        # Return False if the word is not found in the board
        return False
