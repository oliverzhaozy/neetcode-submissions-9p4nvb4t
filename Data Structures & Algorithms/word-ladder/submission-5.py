class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj_list = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                adj_list[pattern].append(word)
        
        q = deque([beginWord])
        visit = set([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neigh in adj_list[pattern]:
                        if neigh not in visit:
                            visit.add(neigh)
                            q.append(neigh)
            res += 1
        
        return 0
