class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to check if a binary tree is a valid BST
        def valid(node, left, right):
            # Base case: If the current node is None, return True
            if not node:
                return True 
            
            # Check if the current node's value is within the valid range
            if not (left < node.val < right):
                return False
            
            # Recursively check the left and right subtrees
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        # Initialize the recursive validation with negative infinity and positive infinity
        return valid(root, float("-inf"), float("inf"))
