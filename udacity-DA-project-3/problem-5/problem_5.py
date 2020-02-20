# Before we start let us reiterate the key components of a Trie or Prefix Tree.
# # A trie is a tree-like data structure that stores a dynamic set of strings.
# # Tries are commonly used to facilitate operations like predictive text or autocomplete
# # features on mobile phones or web search.
# #
# # Before we move into the autocomplete function we need to create a working trie for
# # storing strings. We will create two classes:
# #
# # A Trie class that contains the root node (empty string)
# # A TrieNode class that exposes the general functionality of the Trie,
# # like inserting a word or finding the node which represents a prefix.
# # Give it a try by implementing the TrieNode and Trie classes below!


# Represents a single node in the Trie
class TrieNode():
    def __init__(self):
        self.is_word = False
        self.children = {}

    # Initialize this node in the Trie
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        suffix_results = []

        for char in self.children:
            if self.children[char].is_word:
                suffix_results.append(suffix+char)
            suffix_results += self.children[char].suffixes(suffix+char)
        return suffix_results


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                print(prefix + " not found in word list")
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



prefixNode = MyTrie.find("a")
print(prefixNode.suffixes())
print('---------------------------------------------------------------------')

prefixNode = MyTrie.find("t")
print(prefixNode.suffixes())
print('---------------------------------------------------------------------')

prefixNode = MyTrie.find("fun")
print(prefixNode.suffixes())
print('---------------------------------------------------------------------')

prefixNode = MyTrie.find("")
print(prefixNode.suffixes())
print('---------------------------------------------------------------------')

prefixNode = MyTrie.find("z")
print('--------------------------')


