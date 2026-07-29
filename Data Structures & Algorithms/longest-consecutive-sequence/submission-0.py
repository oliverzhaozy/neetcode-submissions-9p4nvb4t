class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
        
        count, res = 0, 0
        for n in nums:
            if (n - 1) in hashset:
                continue
            
            target = n + 1
            count += 1
            while target in hashset:
                count += 1
                target += 1
            res = max(count, res)
            count = 0
        
        return res

