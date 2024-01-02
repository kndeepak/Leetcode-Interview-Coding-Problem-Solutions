class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, 'slow' and 'fast', both initially pointing to the head of the linked list
        slow = head
        fast = head

        # Use 'fast' to find the middle of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the first half and the reversed second half of the linked list
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # If all values match, the linked list is a palindrome
        return True
