class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj_list = defaultdict(list)
        wordLen = len(wordList[0])

        for i in range(len(wordList)):
            count = 0
            for k in range(wordLen):
                if beginWord[k] != wordList[i][k]:
                    count += 1
            if count == 1:
                adj_list[beginWord].append(wordList[i])
        
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                count = 0 # number of different char btw pairs
                for k in range(wordLen):
                    if wordList[i][k] != wordList[j][k]:
                        count += 1
                if count == 1:
                    adj_list[wordList[i]].append(wordList[j])
                    adj_list[wordList[j]].append(wordList[i])
        
        visited = set()
        queue = deque([beginWord])
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for neighbour in adj_list[word]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        return 0
