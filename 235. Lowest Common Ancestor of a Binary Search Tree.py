# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        cur = root  # Start with the root of the tree.

        while cur:
            # If both p and q values are greater than the current node's value,
            # it means both nodes are in the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right  # Move to the right subtree.
            # If both p and q values are smaller than the current node's value,
            # it means both nodes are in the left subtree.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left  # Move to the left subtree.
            else:
                # If neither of the above conditions is met, it means the current node
                # is the lowest common ancestor since it lies between p and q in the BST.
                return cur

        # If the loop terminates without finding the LCA, return None (although this
        # should not happen for valid inputs where p and q are guaranteed to exist).
        return None
