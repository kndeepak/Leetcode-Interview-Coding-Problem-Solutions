class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        # Define a helper function dfs that constructs a balanced BST from a sorted array
        def dfs(left, right):
            
            # Base case: If the left index is greater than the right index, return None
            if left > right:
                return None
            
            # Calculate the middle index to choose the middle element as the root
            mid = (left + right) // 2

            # Create a new TreeNode with the value of the middle element
            root = TreeNode(nums[mid])
            
            # Recursively build the left subtree with elements to the left of the middle
            root.left = dfs(left, mid - 1)
            
            # Recursively build the right subtree with elements to the right of the middle
            root.right = dfs(mid + 1, right)

            # Return the current root node
            return root
        
        # Call the dfs function initially with the full range of the array
        return dfs(0, len(nums) - 1)
