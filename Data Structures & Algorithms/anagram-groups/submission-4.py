class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) # maps array of 26 chars to strs
        
        for s in strs:
            freq = [0] * 26
            for char in s:
                freq[ord(char) - ord('a')] += 1
            
            hashmap[tuple(freq)].append(s)
        
        return list(hashmap.values())