"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
                    # Create a dictionary 'oldToCopy' to map nodes from the original linked list to their corresponding nodes in the copied linked list.
            # Initialize the mapping for the None node to None since it doesn't have a corresponding copy.
            oldToCopy = {None: None}

            # Initialize a 'cur' pointer to the head of the original linked list.
            cur = head

            # Iterate through the original linked list to create a copy of each node and store it in the 'oldToCopy' dictionary.
            while cur:
                copy = Node(cur.val)  # Create a new node with the same value as the original node.
                oldToCopy[cur] = copy  # Map the original node to its copy in the dictionary.
                cur = cur.next  # Move to the next node in the original linked list.

            # Reset the 'cur' pointer to the head of the original linked list.
            cur = head

            # Iterate through the original linked list again to set the 'next' and 'random' pointers of the copied nodes.
            while cur:
                copy = oldToCopy[cur]  # Get the corresponding copied node from the dictionary.
                copy.next = oldToCopy[cur.next]  # Set the 'next' pointer of the copied node to its corresponding copy.
                copy.random = oldToCopy[cur.random]  # Set the 'random' pointer of the copied node to its corresponding copy's random node.
                cur = cur.next  # Move to the next node in the original linked list.

            # Return the head of the copied linked list, which can be obtained from the dictionary using the original head node.
            return oldToCopy[head]

        
