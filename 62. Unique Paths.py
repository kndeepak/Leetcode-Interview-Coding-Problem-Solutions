class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a list 'row' with 'n' elements, all set to 1. 
        # This represents the number of unique paths to each cell in the bottom row.
        row = [1] * n
        
        # Iterate 'm-1' times as the first row is already initialized.
        for i in range(m - 1):
            # Create a new row 'newrow', initialized similarly to 'row'.
            newrow = [1] * n
            
            # Iterate through the row from the second-last element to the first element.
            for j in range(n - 2, -1, -1):
                # Update the current cell in 'newrow' as the sum of the cell to its right and the cell below it.
                # This represents the total unique paths to the current cell.
                newrow[j] = newrow[j + 1] + row[j]
            
            # Update 'row' to be the 'newrow' for the next iteration.
            # This effectively moves one row up in the grid.
            row = newrow
            
        # Return the number of unique paths to the top-left cell.
        return row[0]
