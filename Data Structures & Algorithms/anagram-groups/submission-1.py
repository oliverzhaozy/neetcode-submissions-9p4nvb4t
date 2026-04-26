class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}

        for string in strs:
            sort = tuple(sorted(string))
            hashmap[sort] = hashmap.get(sort, []) + [string]
                
        return list(hashmap.values())