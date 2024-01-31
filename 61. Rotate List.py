

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head  # No rotation needed for an empty list, single-node list, or k = 0

    # Step 1: Find the length and make the list circular
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    current.next = head  # Make the list circular
    
    # Step 2: Calculate the effective rotation
    k = k % length
    if k == 0:
        current.next = None  # Undo the circular list if no rotation needed
        return head

    # Step 3: Find the new tail (length - k - 1 steps from the head)
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # Step 4: Break the circle
    new_head = new_tail.next
    new_tail.next = None

    return new_head

# Example usage:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

rotated_head = rotateRight(node1, 2)
# Now you can traverse from rotated_head and print values to see the new list
