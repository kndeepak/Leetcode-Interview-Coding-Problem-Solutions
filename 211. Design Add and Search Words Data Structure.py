# Definition for a trie node.
class TrieNode:
    def __init__(self):
        # A dictionary to hold the children nodes. Each key is a character,
        # and the value is the next TrieNode.
        self.children = {}
        # Flag to indicate if a node represents the end of a word.
        self.isEndOfWord = False

# The main class for our data structure.
class WordDictionary:

    def __init__(self):
        # Initialize the root of the trie.
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start from the root node.
        node = self.root
        for char in word:
            # For each character in the word, if the character is not already
            # a child of the current node, add a new node for this character.
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node associated with the current character.
            node = node.children[char]
        # After inserting all characters of the word, mark the last node as
        # an end of a word.
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Define a recursive function for depth-first search.
        def dfs(j, root):
            node = root
            for i in range(j, len(word)):
                char = word[i]
                # If the character is a '.', we must check all possible paths.
                if char == '.':
                    # Check every child node. If any path returns True,
                    # the word exists in the dictionary.
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    # If no paths match, return False.
                    return False
                else:
                    # If the character is not in the children of the current node,
                    # the word does not exist in the dictionary.
                    if char not in node.children:
                        return False
                    # Move to the child node associated with the current character.
                    node = node.children[char]
            # After processing all characters, check if we are at the end of a word.
            return node.isEndOfWord
        # Start the search from the root and the beginning of the word.
        return dfs(0, self.root)
