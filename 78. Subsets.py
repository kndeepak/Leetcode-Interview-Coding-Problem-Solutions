class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store all subsets
        res = []

        # This will be our current subset
        subset = []

        # Define a Depth-First Search (DFS) function to build subsets
        def dfs(i):
            # Base case: if index i reaches the length of nums, 
            # add a copy of the current subset to the result
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include the current element and move to the next element
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude the current element and move to the next element
            subset.pop()
            dfs(i + 1)

        # Start the DFS from the first index
        dfs(0)

        # Return all generated subsets
        return res
