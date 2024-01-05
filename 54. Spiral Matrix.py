class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:
            # Traverse the top row from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse the rightmost column from top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Check if there are more rows to traverse from bottom to top
            if top <= bottom:
                # Traverse the bottom row from right to left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # Check if there are more columns to traverse from left to right
            if left <= right:
                # Traverse the leftmost column from bottom to top
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
