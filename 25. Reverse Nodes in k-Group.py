# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node and set it as the previous node of the current head.
        dummy = ListNode(0, head)
        groupPrev = dummy  # Initialize a pointer 'groupPrev' to the dummy node.

        while True:
            # Get the k-th node from the current 'groupPrev'.
            kth = self.getkth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next  # 'groupNext' points to the next group of nodes.

            prev, cur = kth.next, groupPrev.next  # Initialize 'prev' and 'cur' pointers.

            while cur != groupNext:
                tmp = cur.next  # Store the next node in 'tmp'.
                cur.next = prev  # Reverse the 'next' pointer of 'cur'.
                prev = cur  # Move 'prev' to 'cur'.
                cur = tmp  # Move 'cur' to the next node.

            tmp = groupPrev.next
            groupPrev.next = kth  # Connect the last node of the reversed group to 'groupPrev'.
            groupPrev = tmp  # Move 'groupPrev' to the first node of the next group.

        return dummy.next  # Return the head of the reversed linked list.

    def getkth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
