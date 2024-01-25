# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Initialize two pointers 'slow' and 'fast' to the head of the linked list.
        slow = head
        fast = head.next

        # Move 'slow' by one step and 'fast' by two steps until 'fast' reaches the end of the linked list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 'slow' now points to the middle of the linked list.
        # Create a 'second' pointer to the second half of the linked list and disconnect the first and second halves.
        second = slow.next
        prev = slow.next = None

        # Reverse the second half of the linked list using a 'prev' pointer.
        while second:
            tmp = second.next  # Store the next node in 'tmp'.
            second.next = prev  # Reverse the next pointer of 'second' to point to 'prev'.
            prev = second  # Update 'prev' to 'second'.
            second = tmp  # Move 'second' to the next node.

        # Reconnect the first and second halves of the linked list.
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next  # Store the next nodes in 'tmp1' and 'tmp2'.
            first.next = second  # Connect the 'first' node to the 'second' node.
            second.next = tmp1  # Connect the 'second' node to the original next node of 'first'.
            first, second = tmp1, tmp2  # Move 'first' and 'second' to their respective next nodes.
