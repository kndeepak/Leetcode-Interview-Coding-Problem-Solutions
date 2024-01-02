class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

    
        # Initialize the result list with the first row [1]
        result = [[1]]

        # Loop to generate additional rows
        for i in range(numRows - 1):  # We need to generate numRows - 1 additional rows

            # Create a temporary list 'temp' with 0 added at the beginning and end
            temp = [0] + result[-1] + [0]
            
            # Initialize an empty list 'row' to store the current row being generated
            row = []

            # Loop through 'temp' to calculate the values of the current row
            for j in range(len(result[-1]) + 1):
                # Calculate the value at the current position by summing adjacent elements in 'temp'
                value = temp[j] + temp[j + 1]
                
                # Append the calculated value to the 'row' list
                row.append(value)

            # Append the 'row' to the 'result', representing the next row in the Pascal's Triangle
            result.append(row)

        # Return the final 'result', which contains the entire Pascal's Triangle up to numRows
        return result
