class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Create dummy nodes for left and right ends of the doubly linked list
        self.left, self.right = Node(0, 0), Node(0, 0)
        # Link dummy nodes
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # Remove a node from the doubly linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add(self, node):
        # Add a node right before the right dummy node
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        # Retrieve a value and update its position in the list
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # Insert or update a key-value pair
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        # Check if the cache exceeds the capacity
        if len(self.cache) > self.capacity:
            # Remove the least recently used item
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
