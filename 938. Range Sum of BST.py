

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case: if the root is None (empty tree), return 0
        if not root:
            return 0 

        # If the current node's value is greater than the high limit of the range,
        # skip the right subtree and only process the left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # If the current node's value is less than the low limit of the range,
        # skip the left subtree and only process the right subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If the current node's value is within the range, include it in the sum
        # and continue searching in both left and right subtrees
        return (root.val +
                self.rangeSumBST(root.right, low, high) +
                self.rangeSumBST(root.left, low, high))
