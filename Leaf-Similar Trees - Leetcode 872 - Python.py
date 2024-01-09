class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Define a depth-first search function to collect leaf values
        def dfs(root, leaf):
            # Base case: if the current node is None, return
            if not root:
                return

            # If the node is a leaf (no left or right children), append its value
            if not root.left and not root.right:
                leaf.append(root.val)
                return

            # Recursively call dfs on the left and right children
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        # Initialize two lists to store leaf values of both trees
        leaf1 = []
        leaf2 = []

        # Populate leaf1 and leaf2 with leaf values of root1 and root2
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        # Compare the two leaf sequences for equality
        return leaf1 == leaf2
