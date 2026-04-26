class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s1, s2):
            return sorted(s1) == sorted(s2)

        ans = []
        used = set()

        for i, string in enumerate(strs):
            if i in used:
                continue

            group = [string]

            for j in range(i + 1, len(strs)):
                if j not in used and is_anagram(string, strs[j]):
                    group.append(strs[j])
                    used.add(j)

            ans.append(group)
            
        return ans
            
            
