class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        
        while columnNumber > 0:
            # Calculate the offset by subtracting 1 from columnNumber and taking the remainder when divided by 26
            offset = (columnNumber - 1) % 26
            
            # Convert the offset to the corresponding character and add it to the result
            result += chr(ord('A') + offset)
            
            # Update columnNumber by performing integer division by 26
            columnNumber = (columnNumber - 1) // 26

        # Reverse the result string and return it
        return result[::-1]
