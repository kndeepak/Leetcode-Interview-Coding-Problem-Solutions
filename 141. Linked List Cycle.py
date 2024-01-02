class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, 'slow' and 'fast', both initially pointing to the head of the linked list
        slow = head
        fast = head
        
        # Use a while loop to traverse the linked list with two pointers
        while fast and fast.next:
            # Move the 'slow' pointer one step at a time
            slow = slow.next
            
            # Move the 'fast' pointer two steps at a time
            fast = fast.next.next
            
            # Check if the 'slow' and 'fast' pointers meet at the same node
            if slow == fast:
                # If they meet, it indicates the presence of a cycle in the linked list
                return True
        
        # If the loop completes without finding a cycle, return False
        return False
