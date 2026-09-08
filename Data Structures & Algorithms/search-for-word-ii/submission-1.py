class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
        self.endOfWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        visit = set()
        
        res = []
        def dfs(row, col, node, visit):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit:
                return
            char = board[row][col]
            if char not in node.children:
                return

            visit.add((row, col))
            dfs(row + 1, col, node.children[char], visit)
            dfs(row - 1, col, node.children[char], visit)
            dfs(row, col + 1, node.children[char], visit)
            dfs(row, col - 1, node.children[char], visit)
            visit.remove((row, col))

            node = node.children[char]
            if node.endOfWord:
                res.append(node.word)
                node.endOfWord = False
    
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie.root, visit)
        return res

        