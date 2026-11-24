class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        res = ""
        cur = trie.root
        while len(cur.children) == 1 and not cur.endOfWord:
            char = list(cur.children.keys())[0]
            next_node = cur.children[char]
            res += char
            cur = next_node
        return res
