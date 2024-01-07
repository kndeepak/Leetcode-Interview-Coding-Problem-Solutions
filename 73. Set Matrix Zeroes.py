class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Get the number of rows and columns in the matrix.
        rows, cols = len(matrix), len(matrix[0])
        
        # A flag to mark if the first row contains a zero.
        rowzero = False 
            
        # First pass: check each element in the matrix.
        for r in range(rows):
            for c in range(cols):
                # If an element is zero, set the corresponding first row and first column elements to zero.
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True  # Mark the first row to be zeroed later.

        # Second pass: use the first row and column as markers to set zeroes.
        for r in range(1, rows):
            for c in range(1, cols):
                # If the first element in the row or column is zero, set the current element to zero.
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If the top-left element is zero, zero out the first column.
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # If the first row needs to be zeroed, zero it out.
        if rowzero:
            for c in range(cols):
                matrix[0][c] = 0
