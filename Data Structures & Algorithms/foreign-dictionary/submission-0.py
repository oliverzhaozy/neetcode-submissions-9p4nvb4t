class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []
        
        def dfs(char):
            # Base case
            if char in visited:
                return visited[char] # returns True if cycle, False if already processed

            visited[char] = True # mark as current path 
            for neighbour in adj_list[char]:
                if dfs(neighbour):
                    return True # cycle detected
            
            visited[char] = False # mark as processed (backtracking)
            res.append(char)
            return False

        for char in adj_list:
            if dfs(char):
                return ""
        
        return "".join(res[::-1])